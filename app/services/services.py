from sqlalchemy import select
from sqlalchemy.orm import Session
from app.data.models import Service, ServiceType
from app.schemas.services import ServiceCreate

def service_to_dict(service: Service):
    return {
        "id": service.id,
        "name": service.name,
        "type": service.service_type.name if service.service_type else "unknown",
        "status": service.status
    }

def get_all_services(db: Session):
    statement = select(Service).order_by(Service.id)
    services = db.scalars(statement).all()
    return [service_to_dict(s) for s in services]

def get_service_by_id(db: Session, service_id: int):
    service = db.get(Service, service_id)
    if service is None:
        return None
    return service_to_dict(service)

def get_services_by_status(db: Session, status: str):
    statement = select(Service).where(Service.status == status).order_by(Service.id)
    services = db.scalars(statement).all()
    return [service_to_dict(s) for s in services]

def get_service_type(db: Session, type_name: str):
    statement = select(ServiceType).where(ServiceType.name == type_name)
    return db.scalar(statement)

def create_service(db: Session, service: ServiceCreate):
    service_type = get_service_type(db, service.type)
    if service_type is None:
        return None
    new_service = Service(
        name=service.name,
        type_id=service_type.id,
        status=service.status
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return service_to_dict(new_service)

def update_service(db: Session, service_id: int, service: ServiceCreate):
    current_service = db.get(Service, service_id)
    if current_service is None:
        return None
    service_type = get_service_type(db, service.type)
    if service_type is None:
        return None
    current_service.name = service.name
    current_service.type_id = service_type.id
    current_service.status = service.status
    db.commit()
    db.refresh(current_service)
    return service_to_dict(current_service)

def delete_service(db: Session, service_id: int):
    service = db.get(Service, service_id)
    if service is None:
        return False
    db.delete(service)
    db.commit()
    return True