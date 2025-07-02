# Supabase Setup Guide for Job Application Automation

This guide explains how to set up and connect your Python backend to Supabase for job application automation.

---

## 1. Create Supabase Project

- Go to [https://supabase.com](https://supabase.com)
- Sign up and create a new project (e.g., `job-automation-db`)
- Save your database password and choose the closest region

---

## 2. Create Database Tables

- Open the SQL editor in Supabase dashboard
- Copy and run the SQL commands from `schema.sql` located in `job_application_assistant/backend/schema.sql`
- This will create the following tables:
  - `jobs`
  - `applications`
  - `logs`
  - `users` (optional)

---

## 3. Get API Credentials

- Go to **Settings → API** in Supabase dashboard
- Copy your:
  - Supabase URL endpoint (e.g., `https://your-project-ref.supabase.co`)
  - `anon` public API key

---

## 4. Install Supabase Python Client

```bash
pip install supabase
```

---

## 5. Set Environment Variables

Set the following environment variables in your development environment or `.env` file:

```bash
export SUPABASE_URL="https://your-project-ref.supabase.co"
export SUPABASE_ANON_KEY="your-anon-public-api-key"
```

---

## 6. Use Supabase Client in Python

- The module `job_application_assistant/backend/services/supabase_client.py` provides helper functions to interact with Supabase.
- Example usage:

```python
from supabase_client import insert_job, get_pending_jobs, insert_application, log_event

# Insert a new job
insert_job(
    title="AI Developer",
    company="OpenAI",
    link="https://careers.openai.com/",
    status="Open",
    date="2024-06-30"
)

# Fetch pending jobs
jobs = get_pending_jobs()
print(jobs)

# Log an event
log_event("application", "Applied to AI Developer job")

# Insert an application record
insert_application(job_id=jobs[0]['id'], status="Applied")
```

---

## 7. Integration Tips

- Use these functions in your automation workflow to:
  - Store scraped job listings
  - Track application statuses
  - Log errors and successes
- Extend the module as needed for your specific use cases.

---

This setup provides a fast, reliable, and scalable backend for your job application automation project.
