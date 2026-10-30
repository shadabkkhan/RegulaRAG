from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="RegulaRAG API",
    description="API for the RegulaRAG - The financial regulations assistant",
    version="app_version"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.service_name,
        "version": settings.app_version,
    }


@app.get("/ready")
def readiness_check():
    return{
        "status": "ready",
        "service": settings.service_name,
        "version": settings.app_version,
    }