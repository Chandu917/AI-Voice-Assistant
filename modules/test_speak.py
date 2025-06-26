import unittest
from unittest.mock import patch, MagicMock
import modules.speak as speak_module

class TestSpeak(unittest.TestCase):
    @patch('modules.speak.gTTS')
    @patch('subprocess.run')
    def test_speak(self, mock_run, mock_gtts):
        mock_tts = MagicMock()
        mock_gtts.return_value = mock_tts

        speak_module.speak("Hello world")

        mock_gtts.assert_called_with(text="Hello world", lang='en')
        mock_tts.save.assert_called()
        mock_run.assert_called()

    @patch('speech_recognition.Recognizer.recognize_google')
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Microphone')
    def test_listen_success(self, mock_microphone, mock_listen, mock_recognize):
        mock_recognize.return_value = "test command"
        result = speak_module.listen()
        self.assertEqual(result, "test command")

    @patch('speech_recognition.Recognizer.recognize_google', side_effect=Exception("Error"))
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Microphone')
    @patch('modules.speak.speak')
    def test_listen_exception(self, mock_speak, mock_microphone, mock_listen, mock_recognize):
        result = speak_module.listen()
        mock_speak.assert_called()
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
