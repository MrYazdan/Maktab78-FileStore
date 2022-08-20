from unittest import TestCase

from core.managers import DBManager
from users.models import User


class DBManagerTest(TestCase):

    def setUp(self):
        self.db_manager = DBManager('file_store')

    def test_create_success(self):
        self.u1 = User('Akbar', 'babaii', '0911111212', '1224456786', 20, "ThisIsPassword")
        res = self.db_manager.create(self.u1)

        self.assertIsInstance(res, int)
        self.assertEqual(self.u1.id, res)

    def test_read_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        u = self.db_manager.read(User, self.u1.id)

        self.assertEqual(vars(u), vars(self.u1))

    def test_upgrade_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        new_first_name = 'Reza'
        self.u1.first_name = new_first_name
        self.db_manager.update(self.u1)

        read_u = self.db_manager.read(User, self.u1.id)
        self.assertEqual(read_u.first_name, new_first_name)

    def test_delete_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        id = self.u1.id

        self.db_manager.delete(self.u1)
        self.assertFalse(hasattr(self.u1, 'id'))
        self.assertRaises(Exception, self.db_manager.read, User, id)

    def tearDown(self) -> None:
        try:
            self.db_manager.delete(self.u1)
        except:
            pass
        del self.db_manager
