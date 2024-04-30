from fastapi import Depends
from sqlalchemy.orm import Session
from app.services.date_mappers.port_mapper import PortMapper
from app.services.date_mappers.reservation_mapper import ReservationMapper
from app.services.date_mappers.user_mapper import UserMapper
from app.services.date_mappers.yacht_mapper import YachtMapper
from app.services.repositories.port_repository import PortRepository
from app.services.repositories.reservation_repository import ReservationRepository
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.yacht_repository import YachtRepository
from dependencies.db_dependencies import get_db_session


def get_yacht_repository(
    db: Session = Depends(get_db_session),
    data_mapper: YachtMapper = Depends(YachtMapper),
) -> YachtRepository:
    return YachtRepository(db_session=db, data_mapper=data_mapper)

def get_port_repository(
    db: Session = Depends(get_db_session),
    data_mapper: PortMapper = Depends(PortMapper),
) -> PortRepository:
    return PortRepository(db_session=db, data_mapper=data_mapper)

def get_reservation_repository(
    db: Session = Depends(get_db_session),
    data_mapper: ReservationMapper = Depends(ReservationMapper),
) -> ReservationRepository:
    return ReservationRepository(db_session=db, data_mapper=data_mapper)

def get_user_repository(
    db: Session = Depends(get_db_session),
    data_mapper: UserMapper = Depends(UserMapper),
) -> UserRepository:
    return UserRepository(db_session=db, data_mapper=data_mapper)