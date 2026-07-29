from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ticket_classification():

    payload = {
        "ticket_id": "TCK001",
        "ticket_text": "I was charged twice for my subscription."
    }

    response = client.post(
        "/tickets/classify",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert "ticket_id" in body
    assert "category" in body
    assert "urgency" in body
    assert "sentiment" in body


def test_empty_ticket():

    payload = {
        "ticket_id": "",
        "ticket_text": ""
    }

    response = client.post(
        "/tickets/classify",
        json=payload
    )

    assert response.status_code == 422