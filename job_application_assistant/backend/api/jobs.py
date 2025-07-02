from fastapi import APIRouter, Query
from typing import List

router = APIRouter()

# Dummy job data for demonstration
jobs_data = [
    {"id": 1, "title": "Python Developer", "company": "Tech Corp", "location": "Remote"},
    {"id": 2, "title": "Frontend Engineer", "company": "Web Solutions", "location": "New York"},
    {"id": 3, "title": "Data Scientist", "company": "Data Inc", "location": "San Francisco"},
    {"id": 4, "title": "Backend Developer", "company": "Cloud Services", "location": "Remote"},
]

@router.get("/")
async def get_jobs():
    return {"message": "Jobs endpoint placeholder"}

from fastapi import Query

@router.get("/search-jobs")
async def search_jobs(
    query: str = Query(..., description="Search query for jobs"),
    date_posted: str = Query(None, description="Filter jobs by date posted: '1d', '1w', '1m'"),
    job_type: str = Query(None, description="Filter by job type: 'internship', 'full-time', etc."),
    experience_level: str = Query(None, description="Filter by experience level: 'entry-level', 'fresher'"),
    remote: bool = Query(None, description="Filter for remote jobs"),
):
    # Filter jobs based on query and optional filters
    filtered_jobs = [job for job in jobs_data if query.lower() in job["title"].lower()]

    if date_posted:
        # For demo, filter jobs posted within last 1 day, week, or month
        # Assuming jobs_data has 'date_posted' field in ISO format (YYYY-MM-DD)
        from datetime import datetime, timedelta
        now = datetime.now()
        if date_posted == "1d":
            cutoff = now - timedelta(days=1)
        elif date_posted == "1w":
            cutoff = now - timedelta(weeks=1)
        elif date_posted == "1m":
            cutoff = now - timedelta(days=30)
        else:
            cutoff = None

        if cutoff:
            filtered_jobs = [
                job for job in filtered_jobs
                if "date_posted" in job and datetime.fromisoformat(job["date_posted"]) >= cutoff
            ]

    if job_type:
        filtered_jobs = [
            job for job in filtered_jobs
            if "job_type" in job and job_type.lower() in job["job_type"].lower()
        ]

    if experience_level:
        filtered_jobs = [
            job for job in filtered_jobs
            if "experience_level" in job and experience_level.lower() in job["experience_level"].lower()
        ]

    if remote is not None:
        filtered_jobs = [
            job for job in filtered_jobs
            if "remote" in job and job["remote"] == remote
        ]

    return filtered_jobs
