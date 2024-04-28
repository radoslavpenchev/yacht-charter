from fastapi import Depends
from sqlalchemy.orm import Session
from app.services.date_mappers.yacht_mapper import YachtMapper
from app.services.repositories.yacht_repository import YachtRepository
from dependencies.db_dependencies import get_db_session


def get_yacht_repository(
    db: Session = Depends(get_db_session),
    data_mapper: YachtMapper = Depends(YachtMapper),
) -> YachtRepository:
    return YachtRepository(db_session=db, data_mapper=data_mapper)
