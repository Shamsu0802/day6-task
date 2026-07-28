from fastapi import FastAPI
from app.routers import churn, tickets

app = FastAPI(
    title="AI Pipeline Service"
)

app.include_router(churn.router)
app.include_router(tickets.router, prefix="/tickets")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
