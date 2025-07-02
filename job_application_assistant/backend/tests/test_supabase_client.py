import pytest
from unittest.mock import MagicMock

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from job_application_assistant.backend.services import supabase_client

class MockResponse:
    def __init__(self, data):
        self.data = data

class MockExec:
    def __init__(self, response):
        self.response = response
    def execute(self):
        return self.response

def test_insert_job(monkeypatch: pytest.MonkeyPatch):
    mock_response = MockResponse([{"id": "1234"}])
    mock_exec = MockExec(mock_response)
    monkeypatch.setattr(supabase_client.supabase, "table", lambda table_name: MagicMock(insert=lambda data: mock_exec))

    result = supabase_client.insert_job("Test Job", "Test Company", "http://test.com", "Open", "2024-06-30")
    assert result == [{"id": "1234"}]
