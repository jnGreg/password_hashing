import unittest

from src.password_hashing import PasswordHashing
from src.password_hashing import Connection

ps = PasswordHashing()
cn = Connection()


class PasswordHashingTest(unittest.TestCase):

    #  Connection and database tests section

    def test_if_present_connection(self):
        self.assertIsInstance(cn, Connection)

    def test_hash_not_none(self):
        database = r"\sqlite\db\passwords.db"
        conn = cn.create_connection(database)
        sql = '''SELECT p_id FROM passwords
        ORDER BY p_id DESC LIMIT 1'''
        cur = conn.cursor()
        cur.execute(sql)
        max_id = cur.fetchall()

        for i in range(max_id):
            self.assertIsNotNone(cn.p_hash)

    def test_salt_not_none(self):
        database = r"\sqlite\db\passwords.db"
        conn = cn.create_connection(database)
        sql = '''SELECT p_id FROM passwords
        ORDER BY p_id DESC LIMIT 1'''
        cur = conn.cursor()
        cur.execute(sql)
        max_id = cur.fetchall()

        for i in range(max_id):
            self.assertIsNotNone(cn.p_salt)

    def test_id_exists(self):
        database = r"\sqlite\db\passwords.db"
        conn = cn.create_connection(database)
        sql = '''SELECT p_id FROM passwords
                ORDER BY p_id DESC LIMIT 1'''
        cur = conn.cursor()
        cur.execute(sql)
        max_id = cur.fetchall()

        check_id = 5
        self.assertIn(max_id)


    #  Hashing functions tests section

    def test_if_present_hashing(self):
        self.assertIsInstance(ps, PasswordHashing)

    def test_old_hashing(self):
        database = r"\sqlite\db\passwords.db"
        cn.conn = cn.create_connection(database)
        ps.password = "haslo"
        ps.salt = "sol"

        self.assertEqual(ps.old_hash(cn.conn, ps.password, ps.salt),
                         "65bdae82a9c36b97b4e1a30fa5b201d1bcef17f4613ae8cd51971b048a6aabbb")

    def test_new_hashing(self):
        database = r"\sqlite\db\passwords.db"
        cn.conn = cn.create_connection(database)
        ps.password = "haslo"
        ps.salt = "sol"

        self.assertEqual(ps.new_hash(cn.conn, ps.password, ps.salt),
                         "65bdae82a9c36b97b4e1a30fa5b201d1bcef17f4613ae8cd51971b048a6aabbb")

    def test_pass_check_return(self):
        input_pass = input("please enter password which you want to pass to the function.")
        self.assertEqual(ps.pass_check(), input_pass)












