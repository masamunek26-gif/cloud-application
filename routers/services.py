from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from app.schemas.services import ServiceCreate
from app.services.services import (
    get_all_services,
    get_service_by_id,
    create_service,
    update_service,
    delete_service
)

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

@router.get(
    "",
    summary="Получить список сервисов",
    description="Возвращает полный список сервисов или отфильтрованный по состоянию status."
)
def read_services(
    status: Optional[str] = Query(
        None,
        description="Фильтрация сервисов по состоянию (running, maintenance, stopped)"
    )
):
    return get_all_services(status=status)

@router.get(
    "/{service_id}",
    summary="Получить сервис по идентификатору",
    description="Возвращает сервис с указанным идентификатором.",
    responses={
        404: {"description": "Сервис не найден"}
    }
)
def read_service(
    service_id: int = Path(
        ...,
        description="Уникальный идентификатор сервиса",
        gt=0
    )
):
    service = get_service_by_id(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.post(
    "",
    summary="Создать новый сервис",
    description="Создаёт новый облачный сервис на основе переданных данных.",
    status_code=201
)
def create_service_endpoint(service: ServiceCreate):
    return create_service(service)

@router.put(
    "/{service_id}",
    summary="Изменить сервис",
    description="Изменяет данные существующего сервиса.",
    responses={
        404: {"description": "Сервис не найден"}
    }
)
def update_service_endpoint(service_id: int, service: ServiceCreate):
    updated_service = update_service(service_id, service)
    if updated_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return updated_service

@router.delete(
    "/{service_id}",
    summary="Удалить сервис",
    responses={
        404: {"description": "Сервис не найден"}
    }
)
def delete_service_endpoint(service_id: int):
    deleted_service = delete_service(service_id)
    if deleted_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return {
        "message": "Service deleted",
        "id": service_id
    }
