import unittest
from db_utils import create_connection, run_query
from utils import update_user_token, insert_user, get_user_data, get_topics_data, get_session_token, get_images, \
    get_email


class test_connection(unittest.TestCase):

    def test_get_connection(self):
        conn = create_connection()
        self.assertIsNotNone(conn)

    def test_run_query(self):
        conn = create_connection()
        result = run_query(conn, "select * from users")
        conn.close()
        self.assertIs(type(result), tuple)

    def test_table_topics(self):
        conn = create_connection()
        result = run_query(conn, "select * from topics")
        conn.close()
        self.assertIs(type(result), tuple)

    def test_table_content(self):
        conn = create_connection()
        result = run_query(conn, "select * from content")
        conn.close()
        self.assertIs(type(result), tuple)

    def test_table_user_session(self):
        conn = create_connection()
        result = run_query(conn, "select * from user_session")
        conn.close()
        self.assertIs(type(result), tuple)


if __name__ == '__main__':
    unittest.main()
