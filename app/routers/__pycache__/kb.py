from fastapi import APIRouter

from app.schemas.rag import (
    RAGRequest,
    RAGResponse
)

from app.services.rag_service import ask_kb

router = APIRouter()


@router.post("/ask", response_model=RAGResponse)
def ask(request: RAGRequest):
    return ask_kb(request)