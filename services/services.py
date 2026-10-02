from typing import Optional, List
from app.data.services import services_data
from app.schemas.services import ServiceCreate

def get_all_services(status: Optional[str] = None) -> List[dict]:
    if status:
        return [item for item in services_data if item["status"] == status]
    return services_data

def get_service_by_id(service_id: int) -> Optional[dict]:
    for service in services_data:
        if service["id"] == service_id:
            return service
    return None

def create_service(service: ServiceCreate) -> dict:
    new_id = max((item["id"] for item in services_data), default=0) + 1
    new_service = {
        "id": new_id,
        "name": service.name,
        "type": service.type,
        "status": service.status
    }
    services_data.append(new_service)
    return new_service

def update_service(service_id: int, service: ServiceCreate) -> Optional[dict]:
    for item in services_data:
        if item["id"] == service_id:
            item["name"] = service.name
            item["type"] = service.type
            item["status"] = service.status
            return item
    return None

def delete_service(service_id: int) -> Optional[dict]:
    for item in services_data:
        if item["id"] == service_id:
            services_data.remove(item)
            return item
    return None

def count_services() -> int:
    return len(services_data)
