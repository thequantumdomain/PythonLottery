import unittest
from unittest.mock import patch, MagicMock
from lottery import main

class TestLogic(unittest.TestCase):

    @patch('lottery.fetch_random_users')
    @patch('lottery.update_winner')
    def test_unique_winners_selection(self, mock_update_winner, mock_fetch_random_users):
        mock_user_data = [{'id': i, 'email': f'user{i}@example.com', 'address': {'state': f'State{i}'}} for i in range(1, 26)]
        mock_fetch_random_users.side_effect = [mock_user_data[i:i+5] for i in range(0, len(mock_user_data), 5)]
        
        main()
        
        self.assertEqual(mock_update_winner.call_count, 25)
        # Assuming update_winner logs each call, you could check the log or mock logger to verify unique states

if __name__ == '__main__':
    unittest.main()
