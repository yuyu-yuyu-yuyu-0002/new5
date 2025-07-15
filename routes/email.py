from fastapi import APIRouter

router = APIRouter()

@router.get("/email/ping")
def ping():
    return {"msg": "email route ok"}
