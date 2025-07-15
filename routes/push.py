from fastapi import APIRouter

router = APIRouter()

@router.get("/push/ping")
def ping():
    return {"msg": "push route ok"}
