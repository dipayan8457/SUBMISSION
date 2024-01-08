# backend/app/api/monitoring.py
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# In-memory storage for metrics (Replace with a database in production)
metrics_storage = []

# Function to track API usage metrics
def track_metrics(user_id: int, api_calls: int, data_download_size: int, chatbot_interactions: int):
    metrics_storage.append({
        "user_id": user_id,
        "api_calls": api_calls,
        "data_download_size": data_download_size,
        "chatbot_interactions": chatbot_interactions,
    })

# Endpoint to retrieve API usage statistics for a user
@router.get("/usage_statistics/{user_id}")
def get_usage_statistics(user_id: int):
    # Replace this with actual logic to fetch usage statistics from metrics_storage
    user_metrics = next((metrics for metrics in metrics_storage if metrics["user_id"] == user_id), None)

    if not user_metrics:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user_metrics["user_id"],
        "api_calls": user_metrics["api_calls"],
        "data_download_size": user_metrics["data_download_size"],
        "chatbot_interactions": user_metrics["chatbot_interactions"],
    }

# Endpoint to simulate tracking API usage metrics
@router.post("/simulate_metrics")
def simulate_metrics(users_metrics: List[dict]):
    for metrics in users_metrics:
        track_metrics(
            user_id=metrics["user_id"],
            api_calls=metrics["api_calls"],
            data_download_size=metrics["data_download_size"],
            chatbot_interactions=metrics["chatbot_interactions"],
        )

    return {"message": "Simulated metrics tracked successfully"}
