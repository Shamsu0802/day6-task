from fastapi import APIRouter
from app.schemas.ticket import TicketRequest, TicketResponse
from app.services.ticket_service import classify_ticket

router = APIRouter()

@router.post("/classify", response_model=TicketResponse)
def classify(request: TicketRequest):
    return classify_ticket(request)