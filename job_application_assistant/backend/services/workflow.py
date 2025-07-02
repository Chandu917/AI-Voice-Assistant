from command_parser import parse_job_application_command
from scraper import scrape_linkedin_jobs, scrape_indeed_jobs, scrape_naukri_jobs
from eligibility import check_job_eligibility
from automation import JobApplicationAutomator
import logging
import smtplib
from email.mime.text import MIMEText
import requests

# Placeholder imports for Google Sheets, Airtable, Notion integrations
# from logging_modules import log_to_google_sheets, log_to_airtable, log_to_notion
# from notification_modules import send_email_notification, send_telegram_notification, send_whatsapp_notification

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_job_application_workflow(command_text, user_profile, resume_path, cover_letter_path=None):
    command_params = parse_job_application_command(command_text)
    job_title = command_params.get("job_title")
    locations = command_params.get("locations") or [""]
    companies = command_params.get("companies") or []
    remote_only = command_params.get("remote_only", False)
    eligibility_threshold = command_params.get("eligibility_threshold", 1.0)
    auto_apply = command_params.get("auto_apply", True)

    # Broaden keywords for better scraping results
    broadened_keywords = []
    if job_title:
        lowered = job_title.lower()
        if "python" in lowered:
            broadened_keywords.extend(["python developer", "software engineer", "internship"])
        else:
            broadened_keywords.append(job_title)
    else:
        broadened_keywords.append("python developer")

    all_jobs = []

    for location in locations:
        for keyword in broadened_keywords:
            linkedin_jobs = scrape_linkedin_jobs(keyword, location)
            indeed_jobs = scrape_indeed_jobs(keyword, location)
            naukri_jobs = scrape_naukri_jobs(keyword, location)
            all_jobs.extend(linkedin_jobs + indeed_jobs + naukri_jobs)

    if companies:
        all_jobs = [job for job in all_jobs if job["company"].lower() in [c.lower() for c in companies]]

    if remote_only:
        all_jobs = [job for job in all_jobs if "remote" in job["location"].lower()]

    automator = JobApplicationAutomator(user_profile, resume_path, cover_letter_path)

    applied_jobs = []
    skipped_jobs = []

    for job in all_jobs:
        try:
            eligible, explanation = check_job_eligibility(job.get("title", "") + " " + job.get("company", ""), user_profile)
            if eligible:
                if auto_apply:
                    success = automator.apply_to_linkedin_job(job["link"])
                    if success:
                        applied_jobs.append(job)
                        logger.info(f"Applied to job: {job['title']} at {job['company']}")
                        # log_to_google_sheets(job)
                        # log_to_airtable(job)
                        # log_to_notion(job)
                        # send_email_notification(job)
                        # send_telegram_notification(job)
                        # send_whatsapp_notification(job)
                    else:
                        skipped_jobs.append(job)
                        logger.warning(f"Failed to apply to job: {job['title']} at {job['company']}")
                else:
                    skipped_jobs.append(job)
            else:
                skipped_jobs.append(job)
        except Exception as e:
            logger.error(f"Error processing job {job.get('title', '')} at {job.get('company', '')}: {e}")

    automator.close()

    return {
        "applied_jobs": applied_jobs,
        "skipped_jobs": skipped_jobs,
    }
