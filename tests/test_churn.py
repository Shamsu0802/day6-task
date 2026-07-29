from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_churn_prediction():

    payload = {
        "age": 43,
        "gender": "Male",
        "tenure_months": 14,
        "contract_type": "Month-to-month",
        "payment_method": "Credit card",
        "monthly_charges": 120.52,
        "total_charges": 1688.40,
        "num_support_tickets": 0,
        "tenure_years": 1.166666667,
        "avg_monthly_spend": 112.56,
        "tickets_per_month": 0,
        "tenure_category": "Regular"
    }

    response = client.post(
        "/predict/churn",
        json=payload
    )

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_invalid_churn_request():

    payload = {
        "age": -5,
        "gender": "",
        "tenure_months": -1,
        "contract_type": "",
        "payment_method": "",
        "monthly_charges": -100,
        "total_charges": -10,
        "num_support_tickets": -2,
        "tenure_years": -1,
        "avg_monthly_spend": -10,
        "tickets_per_month": -1,
        "tenure_category": ""
    }

    response = client.post(
        "/predict/churn",
        json=payload
    )

    assert response.status_code == 422