from  unittest import TestCase
from unittest.mock import Mock
from app.controllers.yacht_controller import create_yacht, get_all_yachts, get_yachts
from app.models.entities.yacht import YachtEntity
from app.services.repositories.yacht_repository import YachtFilters
from app.types.dtos.yacht_dtos import CreateYachtPayload
from app.types.enums.country import Country
from app.types.enums.yacht_type import YachtType

class TestYachtController(TestCase):
    def setUp(self):

        self.yacht_repository = Mock()
        self.yacht_repository.insert_one.return_value = None

    def test_create_yacht_success(self):
        body =CreateYachtPayload(
            name="Test Yacht",
            make="Test Make",
            length=50,
            width=10,
            cabins=4,
            passengers=10,
            crew=5,
            type=YachtType.SAILING.value,
            price=1000,
            port_id=1
        )

        response = create_yacht(body=body, yacht_repository=self.yacht_repository)

        self.yacht_repository.insert_one.assert_called_once()

        self.assertEqual(response["message"], "successfully added a yacht: Test Yacht")

    def test_update_yacht_success(self):
        body =CreateYachtPayload(
            name="Test Yacht",
            make="Test Make",
            length=50,
            width=10,
            cabins=4,
            passengers=10,
            crew=5,
            type=YachtType.SAILING.value,
            price=1000,
            port_id=1
        )

        response = create_yacht(body=body, yacht_repository=self.yacht_repository)

        self.yacht_repository.insert_one.assert_called_once()

        self.assertEqual(response["message"], "successfully added a yacht: Test Yacht")
    
    def test_delete_yacht_success(self):
        body =CreateYachtPayload(
            name="Test Yacht",
            make="Test Make",
            length=50,
            width=10,
            cabins=4,
            passengers=10,
            crew=5,
            type=YachtType.SAILING.value,
            price=1000,
            port_id=1
        )

        response = create_yacht(body=body, yacht_repository=self.yacht_repository)

        self.yacht_repository.insert_one.assert_called_once()

        self.assertEqual(response["message"], "successfully added a yacht: Test Yacht")

    def test_get_all_yachts_success(self):
        yacht_rows = [
            YachtEntity(id=1, name="yacht",make="test", length=10, width=10, cabins=3, passengers=5, crew=2, type=YachtType.MOTOR, price=1000, port_id=1),
            YachtEntity(id=2, name="yacht2",make="test", length=10, width=10, cabins=3, passengers=5, crew=2, type=YachtType.MOTOR, price=1500, port_id=1),
            YachtEntity(id=3, name="yacht3",make="test", length=10, width=10, cabins=3, passengers=5, crew=2, type=YachtType.MOTOR, price=2000, port_id=1),
        ]
        self.yacht_repository.get_all.return_value = yacht_rows

        response = get_all_yachts(yacht_repository=self.yacht_repository)

        self.yacht_repository.get_all.assert_called_once()

        self.assertEqual(response, yacht_rows)

    def test_get_yachts_filtered(self):
        yacht_rows = [
            YachtEntity(id=1, name="yacht",make="test", length=15, width=6, cabins=3, passengers=5, crew=2, type=YachtType.MOTOR, price=1000, port_id=1),
            YachtEntity(id=2, name="yacht2",make="test", length=26, width=10, cabins=4, passengers=15, crew=2, type=YachtType.SAILING, price=1500, port_id=1),
            YachtEntity(id=3, name="yacht3",make="test", length=50, width=15, cabins=5, passengers=25, crew=2, type=YachtType.SUPERYACHT, price=2000, port_id=1),
        ]
        self.yacht_repository.get_yachts.return_value = yacht_rows[1]

        response = get_yachts(yacht_repository=self.yacht_repository, port_id=1, length=25, passengers=15, type=YachtType.SAILING, country=Country.BULGARIA)

        self.yacht_repository.get_yachts.assert_called_once_with(filters=YachtFilters(port_id=1, length=25, passengers=15, type=YachtType.SAILING.value, country=Country.BULGARIA.value))

        self.assertEqual(response, yacht_rows[1])