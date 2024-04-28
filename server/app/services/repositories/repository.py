from sqlalchemy.orm import Session

from app.services.date_mappers.data_mapper import DataMapper



class Repository:
    def __init__(self, db_session: Session, data_mapper: DataMapper) -> None:
        super().__init__()
        self.data_mapper = data_mapper
        self.session = db_session
