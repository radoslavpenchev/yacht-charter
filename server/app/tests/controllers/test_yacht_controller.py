from  unittest import TestCase
from unittest.mock import Mock
from app.controllers.yacht_controller import create_yacht
from app.types.dtos.yacht_dtos import CreateYachtPayload
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
            port_id=1
        )

        response = create_yacht(body=body, yacht_repository=self.yacht_repository)

        self.yacht_repository.insert_one.assert_called_once()

        self.assertEqual(response["message"], "successfully added a yacht: Test Yacht")

