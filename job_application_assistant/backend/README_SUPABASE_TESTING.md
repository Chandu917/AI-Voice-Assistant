# Supabase Integration Testing Guide

This document explains how to test the Supabase integration for your job application automation project.

---

## Prerequisites

- Supabase project created with the schema applied.
- Environment variables set:

```bash
export SUPABASE_URL="https://your-project-ref.supabase.co"
export SUPABASE_ANON_KEY="your-anon-public-api-key"
```

- Python dependencies installed:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Tests are located in `job_application_assistant/backend/tests/test_supabase_client.py`.

Run tests using pytest:

```bash
pytest job_application_assistant/backend/tests/test_supabase_client.py
```

---

## What is Tested?

- **Critical-path tests:**
  - Database connection using environment variables.
  - Insert and query operations for `jobs`.
  - Insert operations for `applications`.
  - Logging events in `logs`.
  - User creation and retrieval.

- **Thorough testing:**
  - Handles unique data insertion.
  - Validates data consistency.
  - Checks for successful retrieval of inserted data.

---

## Next Steps

- For **workflow integration testing**, run your Jarvis automation with Supabase connected and verify data flows correctly.
- Monitor logs and application statuses in Supabase dashboard.
- Extend tests as needed for edge cases and error handling.

---

## Troubleshooting

- Ensure environment variables are correctly set.
- Check network connectivity to Supabase.
- Review Supabase dashboard for errors or rate limits.

---

This testing guide helps ensure your Supabase backend is reliable and ready for production use.
