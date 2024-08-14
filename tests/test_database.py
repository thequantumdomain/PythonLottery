import unittest
from unittest.mock import patch, MagicMock
from lottery import init_db, update_winner

class TestDatabase(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_init_db(self, mock_connect):
        init_db()
        mock_connect.assert_called_with('winners.db')

    @patch('sqlite3.connect')
    def test_update_winner(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value
        user_data = {'id': 1, 'email': 'test@example.com', 'address': {'state': 'TestState'}}
        
        update_winner(mock_conn, user_data)
        mock_cursor.execute.assert_called_with('''INSERT OR REPLACE INTO winner (id, email, state) VALUES (?, ?, ?)''', (1, 'test@example.com', 'TestState'))
        mock_conn.commit.assert_called()

if __name__ == '__main__':
    unittest.main()
