from fastapi import FastAPI
from app.config import settings
from app.routers.services import router as services_router
from app.routers.system import router as system_router
from app.routers.objects import router as objects_router
from app.routers.auth import router as auth_router

# Метаданные тегов для документации OpenAPI
tags_metadata = [
    {
        "name": "Services",
        "description": "Операции управления программными сервисами Cloud Application."
    },
    {
        "name": "System",
        "description": "Системные маршруты и сведения о приложении."
    }
]

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.debug
)

# Подключение модулей маршрутизации (роутеров)
app.include_router(services_router)
app.include_router(system_router)
app.include_router(objects_router)
app.include_router(auth_router)