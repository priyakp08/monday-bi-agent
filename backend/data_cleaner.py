import pandas as pd


def clean_board_data(board_data):
    rows = []

    # Get boards from monday.com response
    boards = board_data.get("data", {}).get("boards", [])

    if not boards:
        return pd.DataFrame()

    # Get all items from the board
    items = boards[0]["items_page"]["items"]

    # Convert JSON into rows
    for item in items:
        row = {
            "Name": item["name"]
        }

        for column in item["column_values"]:
            row[column["column"]["title"]] = column["text"]

        rows.append(row)

    # Create DataFrame
    df = pd.DataFrame(rows)

    # Replace empty strings with missing values
    df.replace("", pd.NA, inplace=True)

    # Fill missing values
    df.fillna("Unknown", inplace=True)

    # Remove leading and trailing spaces
    df = df.apply(
        lambda col: col.str.strip() if col.dtype == "object" else col
    )

    return df