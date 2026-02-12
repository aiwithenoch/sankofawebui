from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
async def health():
    return {"status": "ok", "source": "minimal_index"}

@app.get("/api/ping")
async def ping():
    return {"status": "pong"}

@app.get("/api/config")
async def mock_config():
    # Return a minimal config to satisfy the frontend check
    return {"status": True, "version": "0.0.1-minimal"}
