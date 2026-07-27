import os
import requests
from dotenv import load_dotenv
from metrics import generate_metrics

load_dotenv()

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


def get_top_item(data):
    if not data:
        return None

    key = max(data, key=data.get)
    return key, data[key]


def answer_from_metrics(question, metrics):
    q = question.lower()

    # Total Deals
    if "total deals" in q or "how many deals" in q:
        return f"There are {metrics['total_deals']} deals."

    # Total Work Orders
    if "total work orders" in q or "how many work orders" in q:
        return f"There are {metrics['total_workorders']} work orders."

    # Highest Sector
    if "sector" in q and (
        "highest" in q
        or "most" in q
        or "maximum" in q
        or "top" in q
    ):
        sector = get_top_item(metrics.get("sector_distribution", {}))

        if sector:
            return (
                f"{sector[0]} has the highest number of deals "
                f"({sector[1]} deals)."
            )

    # Highest Deal Stage
    if "deal stage" in q and (
        "highest" in q
        or "most" in q
        or "maximum" in q
        or "top" in q
    ):
        stage = get_top_item(metrics.get("deal_stage", {}))

        if stage:
            return (
                f"{stage[0]} has the highest number of deals "
                f"({stage[1]} deals)."
            )

    # Deal Status
    if "deal status" in q:
        status = metrics.get("deal_status", {})

        text = "Deal Status:\n"

        for k, v in status.items():
            text += f"- {k}: {v}\n"

        return text

    # Execution Status
    if "execution status" in q:
        status = metrics.get("execution_status", {})

        text = "Execution Status:\n"

        for k, v in status.items():
            text += f"- {k}: {v}\n"

        return text

    # Billing Status
    if "billing status" in q:
        status = metrics.get("billing_status", {})

        text = "Billing Status:\n"

        for k, v in status.items():
            text += f"- {k}: {v}\n"

        return text

    return None
def ask_gpt(question, deals_df, workorders_df):

    metrics = generate_metrics(deals_df, workorders_df)

    # -----------------------------
    # Answer simple questions directly
    # -----------------------------
    direct_answer = answer_from_metrics(question, metrics)

    if direct_answer:
        return direct_answer

    # -----------------------------
    # Format metrics for AI
    # -----------------------------
    metrics_text = f"""
Business Summary

Total Deals: {metrics.get("total_deals", 0)}
Total Work Orders: {metrics.get("total_workorders", 0)}

Deal Status
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("deal_status", {}).items()])}

Deal Stage
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("deal_stage", {}).items()])}

Sector Distribution
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("sector_distribution", {}).items()])}

Owner Distribution
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("owner_distribution", {}).items()])}

Execution Status
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("execution_status", {}).items()])}

Billing Status
{chr(10).join([f"- {k}: {v}" for k, v in metrics.get("billing_status", {}).items()])}
"""

    prompt = f"""
You are a Business Intelligence Assistant for Skylark Drones.

Use ONLY the information below.

{metrics_text}

Question:
{question}

Rules:

- Never invent numbers.
- Never assume information.
- If the answer is unavailable, clearly say so.
- Answer in business language.
- Keep answers concise.
- Give insights only from the provided metrics.
"""

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert Business Intelligence Assistant. "
                    "Use only the provided metrics. "
                    "Never hallucinate."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,
        "max_tokens": 500
    }

    try:

        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError:
        return f"Hugging Face API Error:\n{response.text}"

    except requests.exceptions.RequestException as e:
        return f"Network Error: {str(e)}"

    except Exception as e:
        return str(e)