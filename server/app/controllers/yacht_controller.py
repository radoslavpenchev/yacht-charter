from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from app.models.entities.yacht import YachtEntity
from app.services.repositories.yacht_repository import YachtRepository
from app.types.dtos.yacht_dtos import CreateYachtPayload, CreateYachtResponse, DeleteYachtResponse, UpdateYachtPayload, UpdateYachtResponse
from app.types.enums.country import Country
from dependencies.repositories_loaders import get_yacht_repository

yacht_controller = APIRouter(prefix="/yachts")

@yacht_controller.post("/", response_model=CreateYachtResponse)
def create_yacht(
    body: CreateYachtPayload,
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
        price=body.price,
        port_id = body.port_id,
    )

    yacht_repository.insert_one(yacht=yacht)

    return {"message": f"successfully added a yacht: {yacht.name}"}
@yacht_controller.patch("/{yacht_id}", response_model=UpdateYachtResponse)
def update_yacht(
    body: UpdateYachtPayload,
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    yacht_id = body.id
    updated_yacht = YachtEntity(
        name = body.name,
        make = body.make,
        length = body.length,
        width = body.width,
        cabins = body.cabins,
        passengers = body.passengers,
        crew = body.crew,
        type = body.type,
        id=yacht_id,
        price=body.price,
        port_id = body.port_id,
    )

    try:
        yacht_repository.update_yacht(yacht=updated_yacht)
        return {"message": f"successfully updated yacht: {updated_yacht.name}"}
    except YachtRepository.NotFound as exc:
        raise HTTPException(status_code=404, detail= "Yacht not found") from exc
    except YachtRepository.AlreadyExists as exc:
        raise HTTPException(status_code=409, detail= "Yacht already exists") from exc

@yacht_controller.get("/", response_model=List[YachtEntity])
def get_all_yachts(
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    yachts = yacht_repository.get_all()
    return yachts

@yacht_controller.get("/{port_id}", response_model=List[YachtEntity])
def get_yachts_by_port(
    port_id: int,
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    yachts = yacht_repository.get_by_port(port_id=port_id)
    return yachts

@yacht_controller.get("/{country}", response_model=List[YachtEntity])
def get_yachts_by_country(
    country: Country,
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    yachts = yacht_repository.get_by_country(country=country.value)
    return yachts
@yacht_controller.delete("/{yacht_id}", response_model=DeleteYachtResponse)
def delete_yacht(
    yacht_id: int,
    yacht_repository: Annotated[
        YachtRepository, Depends(get_yacht_repository)
    ],
):
    try:
        yacht_repository.remove_one(yacht_id=yacht_id)
        return {"message": f"successfully deleted yacht: {yacht_id}"}
    except YachtRepository.NotFound as exc:
        raise HTTPException(status_code=404, detail= "Yacht not found") from exc  