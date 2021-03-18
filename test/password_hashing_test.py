import unittest

from src.password_hashing import PasswordHashing
from src.password_hashing import Connection

ps = PasswordHashing()
cn = Connection()


class PasswordHashingTest(unittest.TestCase):

    def test_if_present(self):
        pass
        self.assertIsInstance(ps, PasswordHashing)

    def test_new_hashing(self):
        ps.password = "haslo"
        ps.salt = "sol"
        self.assertEqual(ps.new_hash(cn.conn, ps.password, ps.salt),
                         "65bdae82a9c36b97b4e1a30fa5b201d1bcef17f4613ae8cd51971b048a6aabbb")

    def test

