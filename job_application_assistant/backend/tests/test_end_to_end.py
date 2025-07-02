import pytest
from unittest.mock import patch, MagicMock

@patch("job_application_assistant.backend.services.notifier.send_notifications")
@patch("job_application_assistant.backend.services.supabase_client.supabase")
def test_full_workflow(mock_supabase, mock_send_notifications):
    # Mock supabase insert and select
    mock_table = MagicMock()
    mock_table.insert.return_value.execute.return_value = {"data": [{"id": "1234"}]}
    mock_table.select.return_value.execute.return_value = {"data": [{"id": "1234", "title": "Software Engineer", "company": "OpenAI"}]}
    mock_supabase.table.return_value = mock_table

    # Mock notifier to simulate successful message sending
    mock_send_notifications.return_value = ["msgid1234"]

    from job_application_assistant.backend.services import workflow_service

    result = workflow_service.run_workflow()
    assert result is True
