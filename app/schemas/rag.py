from pydantic import BaseModel, Field, field_validator


class RAGRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=5000)

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Question cannot be empty.")
        return value


class RAGResponse(BaseModel):
    question: str
    answer: str
    retrieved_doc_ids: list[str]