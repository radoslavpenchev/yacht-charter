from typing import Annotated
from fastapi import APIRouter, Depends
from app.models.entities.yacht import YachtEntity
from app.services.repositories.yacht_repository import YachtRepository
from dependencies.repositories_loaders import get_yacht_repository

yacht_controller = APIRouter(prefix="/yachts")

@yacht_controller.post("/")
def create_yacht(
    body,
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    yacht = YachtEntity(
        name = body.name,
        make = body.make,
        length = body.length,
        width = body.width,
        cabins = body.cabins,
        passengers = body.passengers,
        crew = body.crew,
        type = body.type,
        
        port_id = body.port_id,
    )

    yacht_repository.insert_one(yacht=yacht)

    return {"message": f"successfully added a yacht: {yacht.name}"}
