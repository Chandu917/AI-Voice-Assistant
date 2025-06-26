import unittest
from unittest.mock import patch
from modules.auth import authenticate

class TestAuth(unittest.TestCase):
    @patch('modules.auth.listen')
    @patch('modules.auth.speak')
    def test_authenticate_success(self, mock_speak, mock_listen):
        mock_listen.side_effect = ["i am your boss"]
        result = authenticate()
        self.assertTrue(result)
        mock_speak.assert_any_call("Authentication successful. Welcome back, boss.")

    @patch('modules.auth.listen')
    @patch('modules.auth.speak')
    def test_authenticate_failure(self, mock_speak, mock_listen):
        mock_listen.side_effect = ["wrong passphrase", "wrong passphrase", "wrong passphrase"]
        result = authenticate()
        self.assertFalse(result)
        mock_speak.assert_any_call("Access denied.")

if __name__ == '__main__':
    unittest.main()
