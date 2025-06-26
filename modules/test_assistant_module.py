import unittest
from unittest.mock import patch, MagicMock
import sys
sys.modules['modules.gemini_api'] = __import__('modules.mock_gemini_api')
from modules.assistant import run_jarvis

class TestAssistant(unittest.TestCase):
    @patch('modules.assistant.speak')
    @patch('modules.assistant.listen')
    @patch('modules.assistant.handle_command')
    def test_successful_auth_and_command(self, mock_handle_command, mock_listen, mock_speak):
        # Setup the listen side effects for wake word, passphrase, and command
        mock_listen.side_effect = [
            "hey jarvis",          # wake word
            "i am your boss",      # passphrase
            "open youtube",        # command
            "exit"                 # exit command to stop loop
        ]
        mock_handle_command.return_value = "Opening youtube in Brave."
        mock_speak.return_value = None

        # Run the assistant
        run_jarvis()

        # Check that speak was called with authentication success message
        mock_speak.assert_any_call("Authentication successful, boss. How can I assist you?")
        # Check that handle_command was called with the command
        mock_handle_command.assert_called_with("open youtube")
        # Check that speak was called with the command response
        mock_speak.assert_any_call("Opening youtube in Brave.")
        # Check that speak was called with shutdown message
        mock_speak.assert_any_call("As you command, boss. Shutting down now. Goodbye, boss.")

    @patch('modules.assistant.speak')
    @patch('modules.assistant.listen')
    def test_failed_authentication(self, mock_listen, mock_speak):
        mock_listen.side_effect = [
            "hey jarvis",          # wake word
            "wrong passphrase"     # wrong passphrase
        ]
        mock_speak.return_value = None

        run_jarvis()

        mock_speak.assert_any_call("Authentication failed. Access denied, boss.")

    @patch('modules.assistant.speak')
    @patch('modules.assistant.listen')
    def test_no_wake_word(self, mock_listen, mock_speak):
        mock_listen.return_value = "hello world"
        mock_speak.return_value = None

        run_jarvis()

        mock_speak.assert_any_call("Wake word not detected. Please try again, boss.")

    @patch('modules.assistant.speak')
    @patch('modules.assistant.listen')
    def test_no_command_detected(self, mock_listen, mock_speak):
        mock_listen.side_effect = [
            "hey jarvis",          # wake word
            "i am your boss",      # passphrase
            "",                    # no command detected
            "exit"                 # exit to stop loop
        ]
        mock_speak.return_value = None

        run_jarvis()

        mock_speak.assert_any_call("No command detected. Is there anything else I can assist you with, boss?")

if __name__ == '__main__':
    unittest.main()
