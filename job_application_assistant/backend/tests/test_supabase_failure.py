import pytest
from unittest.mock import MagicMock

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from job_application_assistant.backend.services import supabase_client


def test_supabase_network_failure(monkeypatch):
    # Simulate network failure by raising an exception on execute
    class MockFailExec:
        def execute(self):
            raise ConnectionError("Network failure")
    monkeypatch.setattr(supabase_client.supabase, "table", lambda table_name: MagicMock(insert=lambda data: MockFailExec()))

    with pytest.raises(ConnectionError):
        supabase_client.insert_job("Test Job", "Test Company", "http://test.com", "Open", "2024-06-30")

def test_supabase_wrong_credentials(monkeypatch):
    # Simulate authentication failure by raising an exception
    class MockFailExec:
        def execute(self):
            raise PermissionError("Invalid credentials")
    monkeypatch.setattr(supabase_client.supabase, "table", lambda table_name: MagicMock(insert=lambda data: MockFailExec()))

    with pytest.raises(PermissionError):
        supabase_client.insert_job("Test Job", "Test Company", "http://test.com", "Open", "2024-06-30")
