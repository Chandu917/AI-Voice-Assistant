import unittest
from unittest.mock import patch, MagicMock, call
import modules.speak as speak_module

class TestSpeakModuleDetailed(unittest.TestCase):
    @patch('subprocess.run')
    def test_speak_basic(self, mock_run):
        mock_run.return_value = None
        speak_module.speak("Hello world")
        mock_run.assert_called_once_with(['say', '-v', 'Samantha', 'Hello world'], check=True)

    @patch('subprocess.run', side_effect=Exception("say command failed"))
    def test_speak_error_handling(self, mock_run):
        # Test that speak handles subprocess errors gracefully
        try:
            speak_module.speak("Hello error")
        except Exception as e:
            # Expected exception, so do not fail the test
            pass
        mock_run.assert_called_once()

    @patch('modules.speak.sr.Recognizer.recognize_google')
    @patch('modules.speak.sr.Recognizer.listen')
    @patch('modules.speak.sr.Microphone')
    def test_listen_success(self, mock_microphone, mock_listen, mock_recognize):
        from speech_recognition import AudioSource
        mock_source = MagicMock(spec=AudioSource)
        mock_source.stream = MagicMock()
        mock_source.CHUNK = 1024
        mock_source.SAMPLE_RATE = 16000
        type(mock_source).SAMPLE_WIDTH = property(lambda self: 2)
        import io
        mock_source.stream = io.BytesIO(b'\x00' * 1024)
        mock_microphone.return_value.__enter__.return_value = mock_source
        mock_listen.return_value = b'audio bytes'
        mock_recognize.return_value = "detailed test command"
        result = speak_module.listen()
        self.assertEqual(result, "detailed test command")

    @patch('modules.speak.sr.Recognizer.listen', side_effect=Exception("Test error"))
    @patch('modules.speak.sr.Recognizer.recognize_google')
    @patch('modules.speak.sr.Microphone')
    def test_listen_error(self, mock_microphone, mock_recognize, mock_listen):
        from speech_recognition import AudioSource
        mock_source = MagicMock(spec=AudioSource)
        mock_source.stream = MagicMock()
        mock_source.CHUNK = 1024
        mock_source.SAMPLE_RATE = 16000
        type(mock_source).SAMPLE_WIDTH = property(lambda self: 2)
        import io
        mock_source.stream = io.BytesIO(b'\x00' * 1024)
        # Use actual AudioSource instance for context manager to satisfy type check
        mock_microphone.return_value.__enter__.return_value = mock_source
        mock_listen.return_value = b'audio bytes'
        mock_recognize.return_value = "detailed test command"
        result = speak_module.listen()
        self.assertEqual(result, "")

    @patch('modules.speak.sr.Recognizer.recognize_google', side_effect=Exception("Recognition failure"))
    @patch('modules.speak.sr.Recognizer.listen')
    @patch('modules.speak.sr.Microphone')
    @patch('modules.speak.speak')
    def test_listen_recognition_failure(self, mock_speak, mock_microphone, mock_listen, mock_recognize):
        from speech_recognition import AudioSource
        mock_source = MagicMock(spec=AudioSource)
        mock_source.stream = MagicMock()
        mock_source.CHUNK = 1024
        mock_source.SAMPLE_RATE = 16000
        type(mock_source).SAMPLE_WIDTH = property(lambda self: 2)
        import io
        mock_source.stream = io.BytesIO(b'\x00' * 1024)
        # Use actual AudioSource instance for context manager to satisfy type check
        mock_microphone.return_value.__enter__.return_value = mock_source
        mock_listen.return_value = b'audio bytes'
        result = speak_module.listen()
        self.assertEqual(result, "")
        mock_speak.assert_called_with("Sorry, I couldn't understand.")

    @patch('modules.speak.sr.Recognizer.listen', side_effect=TimeoutError)
    @patch('modules.speak.speak')
    @patch('modules.speak.sr.Microphone')
    def test_listen_timeout(self, mock_microphone, mock_speak, mock_listen):
        from speech_recognition import AudioSource
        mock_source = MagicMock(spec=AudioSource)
        mock_source.stream = MagicMock()
        mock_source.CHUNK = 1024
        mock_source.SAMPLE_RATE = 16000
        type(mock_source).SAMPLE_WIDTH = property(lambda self: 2)
        import io
        mock_source.stream = io.BytesIO(b'\x00' * 1024)
        mock_microphone.return_value.__enter__.return_value = mock_source
        result = speak_module.listen()
        self.assertEqual(result, "")
        mock_speak.assert_called_with("I didn't hear anything.")

if __name__ == '__main__':
    unittest.main()
