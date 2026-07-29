import os
import time
import logging
from openai import OpenAI
from dotenv import load_dotenv
from app.prompts import get_rag_prompt

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_answer(question, retrieved_docs):
    """
    Generate an answer using the retrieved documents.
    Retries the LLM call up to 3 times before returning a fallback response.
    """

    context = "\n\n".join(
        [doc["content"] for doc in retrieved_docs]
    )

    prompt = get_rag_prompt(question, context)

    response = None

    # Retry up to 3 times
    for attempt in range(3):
        try:
            logger.info(f"Calling Groq API (Attempt {attempt + 1})")

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            break

        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed: {e}")

            if attempt < 2:
                time.sleep(2)

    # Fallback if all retries fail
    if response is None:
        logger.error("Groq API unavailable after 3 retries.")

        return (
            "The language model service is temporarily unavailable. "
            "Please try again later."
        )

    try:
        answer = response.choices[0].message.content.strip()

        if not answer:
            raise ValueError("Empty response received from LLM.")

        return answer

    except Exception as e:
        logger.error(f"Error processing LLM response: {e}")

        return (
            "The language model service returned an invalid response. "
            "Please try again later."
        )