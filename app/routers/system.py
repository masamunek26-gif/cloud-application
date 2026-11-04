from fastapi import APIRouter
from app.config import APP_NAME, APP_VERSION
from app.services.services import count_services

router = APIRouter(
    tags=["System"]
)

@router.get("/", summary="Главный эндпоинт")
def root():
    return {"application": APP_NAME, "version": APP_VERSION, "status": "running"}

@router.get("/status", summary="Состояние сервера")
def status():
    return {"status": "ok", "service": APP_NAME}

@router.get("/about", summary="Информация о приложении")
def about():
    return {
        "name": APP_NAME,
        "type": "server application",
        "language": "Python",
        "framework": "FastAPI"
    }

@router.get("/course", summary="Сведения об учебном курсе")
def course():
    return {
        "discipline": "Управление работами и разработка программного обеспечения облачных систем",
        "laboratory": 7,
        "project": APP_NAME
    }

# Доп. задание повышенной сложности
@router.get("/service-count", summary="Количество сервисов")
def service_count():
    return {"services": count_services()}