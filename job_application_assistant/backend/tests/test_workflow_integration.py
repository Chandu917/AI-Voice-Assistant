import pytest
from unittest.mock import patch, MagicMock

@patch("job_application_assistant.backend.services.supabase_client.supabase")
def test_workflow_integration(mock_supabase):
    # Mock supabase response
    mock_table = MagicMock()
    mock_table.select.return_value.execute.return_value = {"data": [{"id": "1234", "title": "Test Job"}]}
    mock_supabase.table.return_value = mock_table

    # Import the workflow function to test
    from job_application_assistant.backend.services import workflow_service

    # Assuming workflow_service has a run_workflow function
    result = workflow_service.run_workflow()
    assert result is True
