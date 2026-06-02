import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import router as api_router

# 🚀 Configure logging to track requests in Railway logs
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)
logger.info("🚀 Booting up S.A.N.E.-AI Backend...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 🚀 PRODUCTION CORS FIX
# We hardcode the origins here to ensure the browser preflight check passes.
origins = [
    "https://kpcl-chatbot.vercel.app",  # Your live frontend
    "http://localhost:5173",            # Local Vite development
    "http://127.0.0.1:5173",          # Local fallback
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Include the API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

# Root health check to verify backend is awake
@app.get("/")
async def root():
    return {"status": "online", "message": "KPCL Chatbot Backend is running"}

if __name__ == "__main__":
    import uvicorn
    # Use 'main:app' to ensure uvicorn finds the file correctly in Railway
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)