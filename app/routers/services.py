from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.data.database import get_db
from app.schemas.services import ServiceCreate
from app.services.services import (
    create_service,
    delete_service,
    get_all_services,
    get_service_by_id,
    update_service
)

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("", summary="Получить список сервисов")
def read_services(db: Session = Depends(get_db)):
    return get_all_services(db)

@router.get("/{service_id}", summary="Получить сервис по идентификатору")
def read_service(
    service_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    service = get_service_by_id(db, service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.post("", summary="Создать новый сервис", status_code=201)
def create_service_endpoint(
    service: ServiceCreate,
    db: Session = Depends(get_db)
):
    created_service = create_service(db, service)
    if created_service is None:
        raise HTTPException(status_code=400, detail="Service type not found")
    return created_service

@router.put("/{service_id}", summary="Изменить сервис")
def update_service_endpoint(
    service_id: int,
    service: ServiceCreate,
    db: Session = Depends(get_db)
):
    updated_service = update_service(db, service_id, service)
    if updated_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return updated_service

@router.delete("/{service_id}", summary="Удалить сервис")
def delete_service_endpoint(
    service_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_service(db, service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted", "id": service_id}