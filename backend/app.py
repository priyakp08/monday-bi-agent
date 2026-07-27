from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from monday_client import (
    get_board_data,
    DEALS_BOARD_ID,
    WORK_ORDERS_BOARD_ID,
)

from data_cleaner import clean_board_data
from ai_agent import ask_gpt

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Monday.com Business Intelligence Agent is running!"
    }


@app.get("/deals")
def get_deals():
    board_data = get_board_data(DEALS_BOARD_ID)
    df = clean_board_data(board_data)
    return df.to_dict(orient="records")


@app.post("/ask")
def ask_question(request: QueryRequest):
    deals_df = clean_board_data(get_board_data(DEALS_BOARD_ID))
    workorders_df = clean_board_data(get_board_data(WORK_ORDERS_BOARD_ID))

    answer = ask_gpt(
        request.question,
        deals_df,
        workorders_df
    )

    return {
        "answer": answer
    }


@app.get("/board-info/deals")
def deals_info():
    data = get_board_data(DEALS_BOARD_ID)
    return {
        "board_name": data["data"]["boards"][0]["name"],
        "item_count": len(data["data"]["boards"][0]["items_page"]["items"])
    }


@app.get("/board-info/workorders")
def workorders_info():
    data = get_board_data(WORK_ORDERS_BOARD_ID)
    return {
        "board_name": data["data"]["boards"][0]["name"],
        "item_count": len(data["data"]["boards"][0]["items_page"]["items"])
    }


@app.get("/workorders-columns")
def workorders_columns():
    board_data = get_board_data(WORK_ORDERS_BOARD_ID)
    df = clean_board_data(board_data)

    return {
        "columns": list(df.columns)
    }


@app.get("/deals-columns")
def deals_columns():
    board_data = get_board_data(DEALS_BOARD_ID)
    df = clean_board_data(board_data)

    return {
        "columns": list(df.columns)
    }


@app.get("/deals-client-codes")
def deals_client_codes():
    df = clean_board_data(get_board_data(DEALS_BOARD_ID))
    return df["Client Code"].drop_duplicates().tolist()


@app.get("/workorders-client-codes")
def workorders_client_codes():
    df = clean_board_data(get_board_data(WORK_ORDERS_BOARD_ID))
    return df["Customer Name Code"].drop_duplicates().tolist()
