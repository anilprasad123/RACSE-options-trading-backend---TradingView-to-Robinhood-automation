from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def webhook_handler(request: Request):
    payload = await request.json()
    # TODO: Process RACSE signal
    return {"status": "received", "signal": payload.get("signal", "NONE")}
