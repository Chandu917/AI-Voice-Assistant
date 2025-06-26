import unittest
from unittest.mock import patch
from modules.command_handler import handle_command

class TestCommandHandler(unittest.TestCase):
    @patch('modules.command_handler.open_app')
    @patch('modules.command_handler.open_website_in_brave')
    @patch('modules.command_handler.ask_gemini')
    def test_handle_command_open_app(self, mock_ask_gemini, mock_open_website, mock_open_app):
        mock_open_app.return_value = True
        mock_ask_gemini.return_value = '{"intent": "open_app", "target": "brave"}'
        response = handle_command("open app brave")
        self.assertIn("Opening", response)

    @patch('modules.command_handler.open_app')
    @patch('modules.command_handler.open_website_in_brave')
    @patch('modules.command_handler.ask_gemini')
    def test_handle_command_open_website(self, mock_ask_gemini, mock_open_website, mock_open_app):
        mock_open_website.return_value = True
        mock_ask_gemini.return_value = '{"intent": "open_website", "target": "youtube"}'
        response = handle_command("open website youtube")
        self.assertIn("opening youtube in brave", response.lower())

    @patch('modules.command_handler.ask_gemini')
    def test_handle_command_shutdown(self, mock_ask_gemini):
        mock_ask_gemini.return_value = '{"intent": "shutdown"}'
        with self.assertRaises(SystemExit):
            handle_command("shutdown")

    @patch('modules.command_handler.ask_gemini')
    def test_handle_command_unknown(self, mock_ask_gemini):
        mock_ask_gemini.return_value = ''
        response = handle_command("some unknown command")
        self.assertEqual(response, "Command not recognized.")

if __name__ == '__main__':
    unittest.main()
