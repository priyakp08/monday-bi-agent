import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORK_ORDERS_BOARD_ID = os.getenv("WORK_ORDERS_BOARD_ID")

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

def get_board_data(board_id):
    query = """
    query ($boardId: ID!) {
      boards(ids: [$boardId]) {
        name
        items_page {
          items {
            id
            name
            column_values {
              column {
                title
              }
              text
            }
          }
        }
      }
    }
    """

    variables = {
        "boardId": board_id
    }

    response = requests.post(
        URL,
        json={
            "query": query,
            "variables": variables
        },
        headers=HEADERS
    )

    return response.json()