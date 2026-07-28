from fastapi import APIRouter
from app.schemas.churn import ChurnRequest, ChurnResponse
from app.services.churn_service import predict_churn

router = APIRouter()


@router.post("/predict/churn", response_model=ChurnResponse)
def predict(request: ChurnRequest):
    return predict_churn(request)