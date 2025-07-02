import pytest
from unittest.mock import patch
import os

@patch("job_application_assistant.backend.services.twilio_service.Client")
def test_twilio_api_failure(mock_client_class):
    # Set dummy environment variables for Twilio
    os.environ["TWILIO_ACCOUNT_SID"] = "dummy_sid"
    os.environ["TWILIO_AUTH_TOKEN"] = "dummy_token"
    os.environ["TWILIO_PHONE_NUMBER"] = "+1234567890"

    # Mock the Client instance and its messages.create method to raise an exception
    mock_client = mock_client_class.return_value
    mock_client.messages.create.side_effect = Exception("Twilio API failure")

    from job_application_assistant.backend.services import notifier

    with pytest.raises(Exception) as exc_info:
        notifier.send_notifications(["+1234567890"], "Test message")
    assert "Twilio API failure" in str(exc_info.value)
