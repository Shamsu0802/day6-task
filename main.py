from fastapi import FastAPI

from app.routers import (
    churn,
    tickets,
    kb
)

from app.logger import log_requests

app = FastAPI(
    title="AI Pipeline Service"
)

# Register logging middleware
app.middleware("http")(log_requests)

# Register routers
app.include_router(churn.router)
app.include_router(tickets.router, prefix="/tickets")
app.include_router(kb.router, prefix="/kb")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }