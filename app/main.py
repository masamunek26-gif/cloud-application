from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION
from app.routers.services import router as services_router
from app.routers.system import router as system_router

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
    title=APP_NAME,
    version=APP_VERSION,
    description="Учебное серверное приложение для изучения разработки программного обеспечения облачных систем.",
    openapi_tags=tags_metadata
)

# Подключение модулей маршрутизации (роутеров)
app.include_router(services_router)
app.include_router(system_router)