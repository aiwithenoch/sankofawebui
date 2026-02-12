import os
import sys
from fastapi import FastAPI, Request

# Add the backend directory to the sys.path so we can import open_webui
current_dir = os.path.dirname(__file__)
backend_dir = os.path.abspath(os.path.join(current_dir, '..', 'backend'))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

app = FastAPI()

try:
    from open_webui.main import app as webui_app
    # Mount the main app or just use it
    app = webui_app
    print("Successfully imported open_webui.main")
except Exception as e:
    print(f"Failed to import open_webui.main: {e}")
    # Fallback app to report errors
    @app.get("/api/health")
    async def health():
        return {"status": "error", "error": str(e), "source": "index_py_fallback"}

@app.get("/api/health")
async def health():
    return {"status": "ok", "message": "Backend is running on Vercel (Full App)"}

@app.get("/api/ping")
async def ping():
    return {"status": "pong"}
