from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_rag():

    payload = {
        "question": "How do I reset my password?"
    }

    response = client.post(
        "/kb/ask",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert "question" in body
    assert "answer" in body
    assert "retrieved_doc_ids" in body


def test_empty_question():

    payload = {
        "question": ""
    }

    response = client.post(
        "/kb/ask",
        json=payload
    )

    assert response.status_code == 422