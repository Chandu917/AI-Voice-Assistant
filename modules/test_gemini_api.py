import unittest
from unittest.mock import patch, MagicMock
from modules.gemini_api import ask_gemini

class TestGeminiAPI(unittest.TestCase):
    @patch('modules.gemini_api.model.generate_content')
    def test_ask_gemini_success(self, mock_generate_content):
        mock_response = MagicMock()
        mock_response.text = "This is a response"
        mock_generate_content.return_value = mock_response

        response = ask_gemini("Hello")
        self.assertEqual(response, "This is a response")

    @patch('modules.gemini_api.model.generate_content')
    def test_ask_gemini_exception(self, mock_generate_content):
        mock_generate_content.side_effect = Exception("API error")

        response = ask_gemini("Hello")
        self.assertTrue(response.startswith("Error with Gemini:"))

if __name__ == '__main__':
    unittest.main()
