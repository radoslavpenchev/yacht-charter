
from app.models.db.port import Port
from app.models.entities.yacht import YachtEntity
from app.services.date_mappers.yacht_mapper import YachtMapper
from app.services.repositories.yacht_repository import YachtRepository
from app.tests.repositories import RepositoryTestCase
from app.types.enums.yacht_type import YachtType


class TestYachtRepository(RepositoryTestCase):
    def setUp(self):
        super().setUp()
        self.data_mapper = YachtMapper()
        self.repository = YachtRepository(db_session= self.session, data_mapper=self.data_mapper)
        self.port = Port(id=1, name="port")
        self.session.add(self.port)
        self.session.commit()
    
    def test_insert_one_correctly(self):
        yacht = YachtEntity(id=1, name="yacht",make="test", length=10, width=10, cabins=3, passengers=5, crew=2, type=YachtType.MOTOR, port_id=1)
        self.repository.insert_one(yacht)
        
        yacht_model = self.session.query(YachtEntity).filter_by(name ="yacht").first()
        mapped_model = self.data_mapper.to_entity(yacht_model)
        self.assertEqual(yacht, mapped_model)