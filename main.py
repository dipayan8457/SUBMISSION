# backend/app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins (replace * with your frontend's origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Endpoint to track API usage metrics
@app.post("/track_metrics/{user_id}")
def track_api_usage_metrics(user_id: int, api_calls: int, data_download_size: int, chatbot_interactions: int):
    # Validate input (you may add more validation logic)
    if api_calls < 0 or data_download_size < 0 or chatbot_interactions < 0:
        raise HTTPException(status_code=400, detail="Metrics cannot be negative")

    # Track metrics
    track_metrics(user_id, api_calls, data_download_size, chatbot_interactions)

    # HTML response with inline styles
    return HTMLResponse(
        content=f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 20px;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    p {{
                        color: #555;
                    }}
                </style>
            </head>
            <body>
                <h1>Metrics Tracked Successfully</h1>
                <p>User ID: {user_id}</p>
                <p>API Calls: {api_calls}</p>
                <p>Data Download Size: {data_download_size}</p>
                <p>Chatbot Interactions: {chatbot_interactions}</p>
            </body>
        </html>
        """,
        status_code=200,
    )
