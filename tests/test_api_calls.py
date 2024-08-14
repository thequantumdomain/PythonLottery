import unittest
from unittest.mock import patch, MagicMock  # Ensure MagicMock is imported
import requests
from lottery import fetch_random_users

class TestAPICalls(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_random_users(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{'id': 1, 'email': 'test@example.com', 'address': {'state': 'TestState'}}]
        mock_get.return_value = mock_response
        
        users = fetch_random_users(1)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['email'], 'test@example.com')
        mock_get.assert_called_with('https://random-data-api.com/api/users/random_user', params={'size': 1})

if __name__ == '__main__':
    unittest.main()
