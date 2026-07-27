from monday_client import (
    get_board_data,
    DEALS_BOARD_ID,
    WORK_ORDERS_BOARD_ID
)

from data_cleaner import clean_board_data
import pandas as pd


def get_deals_dataframe():
    board_data = get_board_data(DEALS_BOARD_ID)
    return clean_board_data(board_data)


def get_workorders_dataframe():
    board_data = get_board_data(WORK_ORDERS_BOARD_ID)
    return clean_board_data(board_data)


def answer_query(question):
    deals_df = get_deals_dataframe()
    workorders_df = get_workorders_dataframe()

    question = question.lower()

    # Total Deals
    if "total deals" in question:
        return {
            "answer": f"Total deals: {len(deals_df)}"
        }

    # Total Work Orders
    elif "total work orders" in question:
        return {
            "answer": f"Total work orders: {len(workorders_df)}"
        }

    # Open Deals
    elif "open deals" in question:

        if "Deal Status" in deals_df.columns:

            open_deals = deals_df[
                deals_df["Deal Status"] == "Open"
            ]

            return {
                "answer": f"Open deals: {len(open_deals)}"
            }

        return {
            "answer": "Deal Status column not found."
        }

    # Total Revenue
    elif "revenue" in question or "deal value" in question:

        if "Masked Deal value" in deals_df.columns:

            values = pd.to_numeric(
                deals_df["Masked Deal value"]
                .astype(str)
                .str.replace(",", ""),
                errors="coerce"
            ).fillna(0)

            return {
                "answer": f"Total Deal Value: {values.sum():,.2f}"
            }

        return {
            "answer": "Deal value column not found."
        }

    # Cross-board Query
    elif "clients in both boards" in question:

        if (
            "Client Code" in deals_df.columns
            and
            "Customer Name Code" in workorders_df.columns
        ):

            merged = deals_df.merge(
                workorders_df,
                left_on="Client Code",
                right_on="Customer Name Code",
                how="inner"
            )

            clients = (
                merged["Client Code"]
                .drop_duplicates()
                .tolist()
            )

            return {
                "answer": f"{len(clients)} clients are present in both boards.",
                "clients": clients
            }

        return {
            "answer": "Required columns not found."
        }

    # Default Response
    return {
        "answer": "Sorry, I don't understand that question yet."
    }