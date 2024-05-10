from unittest import TestCase

from app.database import get_engine, get_session_maker


class RepositoryTestCase(TestCase):
    def setUp(self):
        self.connection = get_engine().connect()

        self.trans = self.connection.begin()

        session_local = get_session_maker()
        self.session = session_local(
            bind=self.connection, join_transaction_mode="create_savepoint"
        )

    def tearDown(self):
        self.session.close()

        self.trans.rollback()

        self.connection.close()
