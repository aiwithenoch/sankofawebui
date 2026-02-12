import os
import sys
from fastapi import Request

# Add the backend directory to the sys.path so we can import open_webui
current_dir = os.path.dirname(__file__)
backend_dir = os.path.abspath(os.path.join(current_dir, '..', 'backend'))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

from open_webui.main import app

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running on Vercel"}

@app.get("/api/ping")
async def ping():
    return {"status": "pong"}
