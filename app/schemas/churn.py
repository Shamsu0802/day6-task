from pydantic import BaseModel

class ChurnRequest(BaseModel):
    age: int
    gender: str
    tenure_months: int
    contract_type: str
    payment_method: str
    monthly_charges: float
    total_charges: float
    num_support_tickets: int
    tenure_years: float
    avg_monthly_spend: float
    tickets_per_month: float
    tenure_category: str


class ChurnResponse(BaseModel):
    prediction: str