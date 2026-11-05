from fastapi import APIRouter, Request
from app.config import settings

router = APIRouter()

@router.get("/status")
def status():
    return {
        "status": "ok",
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "debug": settings.debug
    }

@router.get("/connection", summary="Информация о соединении")
def connection_info(request: Request):
    return {
        "scheme": request.url.scheme,
        "host": request.url.hostname,
        "secure": request.url.scheme == "https"
    }