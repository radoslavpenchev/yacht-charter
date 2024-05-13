from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.entities.port import PortEntity
from app.services.repositories.port_repository import PortRepository
from app.types.dtos.port_dtos import CreatePortPayload, CreatePortResponse, DeletePortResponse
from dependencies.repositories_loaders import get_port_repository


port_controller = APIRouter(prefix="/ports")

@port_controller.post("/", response_model=CreatePortResponse)
def create_port(
    body: CreatePortPayload,
    port_repository: Annotated[
        PortRepository, Depends(get_port_repository)
    ],
):
    port = PortEntity(
        name = body.name,
        country = body.country,
        town = body.town,
    )
    try:
        port_repository.insert_one(port=port)
        return {"message": f"successfully added a port: {body.name}"}
    except PortRepository.AlreadyExists as exc:
        return {"message": f"Port already exists"}
    
@port_controller.delete("/{port_id}", response_model=DeletePortResponse)
def delete_port(
    port_id: int,
    port_repository: Annotated[
        PortRepository, Depends(get_port_repository)
    ],
):
    try:
        port_repository.remove_one(port_id=port_id)
        return {"message": f"successfully deleted port: {port_id}"}
    except PortRepository.NotFound as exc:
        return {"message": f"Port not found"}