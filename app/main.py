from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.webhook_router import router as webhook_router
from app.routers.status_router import router as status_router
from app.routers.admin_router import router as admin_router
from app.tasks.scheduler import start_scheduler

app = FastAPI(title="RACSE Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(webhook_router, prefix="/webhook", tags=["webhook"])
app.include_router(status_router, prefix="/status", tags=["status"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

# Start scheduled exit automation
start_scheduler(app)

@app.get("/")
async def root():
    return {"status": "RACSE backend running"}
