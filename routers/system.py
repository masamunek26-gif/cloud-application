from fastapi import APIRouter
from app.config import APP_NAME
from app.services.services import count_services

router = APIRouter(
    tags=["System"]
)

@router.get("/status", summary="Получить статус приложения")
def status():
    return {
        "status": "ok",
        "service": APP_NAME
    }

@router.get("/about", summary="Информация о приложении")
def about():
    return {
        "name": APP_NAME,
        "type": "server application",
        "language": "Python",
        "framework": "FastAPI"
    }

@router.get("/course", summary="Информация о курсе")
def course():
    return {
        "discipline": "Управление работами и разработка программного обеспечения облачных систем",
        "laboratory": 10,
        "project": APP_NAME
    }

@router.get("/service-count", summary="Количество сервисов")
def get_service_count():
    return {
        "services": count_services()
    }
