import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

valid_categories = [
    "Billing",
    "Technical Issue",
    "Account Access",
    "Feature Request",
    "Complaint",
    "General Inquiry"
]

valid_urgencies = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

valid_sentiments = [
    "Positive",
    "Neutral",
    "Negative"
]


def get_zero_shot_prompt(ticket_id, ticket_text):
    return f"""
You are a customer support ticket classifier.

Classify the following customer support ticket.

Rules:
- Choose EXACTLY ONE category.
- Return ONLY valid JSON.
- Do not include explanations.
- Do not use markdown.

Schema:

{{
    "ticket_id": "{ticket_id}",
    "category": "Billing | Technical Issue | Account Access | Feature Request | Complaint | General Inquiry",
    "urgency": "Low | Medium | High | Critical",
    "sentiment": "Positive | Neutral | Negative"
}}

Ticket:
{ticket_text}
"""


def classify_ticket(request):
    prompt = get_zero_shot_prompt(
        request.ticket_id,
        request.ticket_text
    )

    response = None

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )
            break

        except Exception:
            if attempt < 2:
                time.sleep(3)

    if response is None:
        raise Exception("Groq API failed after 3 retries.")

    response_text = response.choices[0].message.content.strip()
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()

    result = json.loads(response_text)

    if result["category"] not in valid_categories:
        raise ValueError("Invalid category returned.")

    if result["urgency"] not in valid_urgencies:
        raise ValueError("Invalid urgency returned.")

    if result["sentiment"] not in valid_sentiments:
        raise ValueError("Invalid sentiment returned.")

    return result