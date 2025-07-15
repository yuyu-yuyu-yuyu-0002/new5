from fastapi import APIRouter

router = APIRouter()

@router.get("/reminder/ping")
def ping():
    return {"msg": "reminder route ok"}
