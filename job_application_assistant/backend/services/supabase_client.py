"""
Supabase client integration for Job Application Automation

This module provides connection setup and example functions to interact with Supabase tables:
- jobs
- applications
- logs
- users (optional)

Usage:
- Set environment variables SUPABASE_URL and SUPABASE_ANON_KEY before running.
- Install supabase client: pip install supabase
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
from typing import Optional, List, Dict
from datetime import datetime

load_dotenv()  # Load environment variables from .env file

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://test.supabase.co")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "testanonkey")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def insert_job(title: str, company: str, link: str, status: str, date: str) -> Dict:
    """
    Insert a new job listing into the jobs table.
    date should be in ISO format: YYYY-MM-DD
    """
    data = {
        "title": title,
        "company": company,
        "link": link,
        "status": status,
        "date": date
    }
    response = supabase.table("jobs").insert(data).execute()
    if isinstance(response, list):
        return response[0]
    return getattr(response, "data", None)

def get_pending_jobs() -> List[Dict]:
    """
    Fetch jobs with status 'Open' or 'Pending' to apply.
    """
    response = supabase.table("jobs").select("*").in_("status", ["Open", "Pending"]).execute()
    if isinstance(response, list):
        return response[0]
    return getattr(response, "data", None)

def insert_application(job_id: str, applied_at: Optional[str] = None, status: str = "Applied", notes: Optional[str] = None) -> Dict:
    """
    Insert a new application record.
    applied_at should be ISO datetime string, defaults to now if None.
    """
    if applied_at is None:
        applied_at = datetime.utcnow().isoformat()
    data = {
        "job_id": job_id,
        "applied_at": applied_at,
        "status": status,
        "notes": notes
    }
    response = supabase.table("applications").insert(data).execute()
    return response.data

def log_event(event_type: str, message: str, timestamp: Optional[str] = None) -> Dict:
    """
    Insert a log event.
    timestamp should be ISO datetime string, defaults to now if None.
    """
    if timestamp is None:
        timestamp = datetime.utcnow().isoformat()
    data = {
        "event_type": event_type,
        "message": message,
        "timestamp": timestamp
    }
    response = supabase.table("logs").insert(data).execute()
    return response.data

def get_user(user_id: str) -> Optional[Dict]:
    """
    Fetch user by id.
    """
    response = supabase.table("users").select("*").eq("id", user_id).single().execute()
    return response.data

def create_user(user_id: str, name: str, email: str) -> Dict:
    """
    Create a new user.
    """
    data = {
        "id": user_id,
        "name": name,
        "email": email,
        "created_at": datetime.utcnow().isoformat()
    }
    response = supabase.table("users").insert(data).execute()
    return response.data
