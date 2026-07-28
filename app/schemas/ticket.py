from pydantic import BaseModel

class TicketRequest(BaseModel):
    ticket_id: str
    ticket_text: str


class TicketResponse(BaseModel):
    ticket_id: str
    category: str
    urgency: str
    sentiment: str