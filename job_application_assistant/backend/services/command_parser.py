import re

def parse_job_application_command(command_text):
    """
    Parses natural language commands related to job applications.
    Returns a dict with extracted parameters like:
    - job_title
    - locations
    - companies
    - remote_only (bool)
    - eligibility_threshold (float)
    - auto_apply (bool)
    """
    command_text = command_text.lower()

    job_title_match = re.search(r"(apply for|search|look for|find|check for)\\s+(.*?)\\s+(jobs|roles|positions)", command_text)
    job_title = job_title_match.group(2) if job_title_match else None

    locations = re.findall(r"in ([a-z\\s]+)", command_text)
    companies = re.findall(r"at ([a-z\\s,]+)", command_text)
    remote_only = "remote" in command_text

    eligibility_threshold = 1.0  # default 100%
    threshold_match = re.search(r"meet (\\d+)%", command_text)
    if threshold_match:
        eligibility_threshold = float(threshold_match.group(1)) / 100.0

    auto_apply = not ("confirm" in command_text or "wait for" in command_text)

    return {
        "job_title": job_title,
        "locations": locations,
        "companies": [c.strip() for c in companies[0].split(",")] if companies else [],
        "remote_only": remote_only,
        "eligibility_threshold": eligibility_threshold,
        "auto_apply": auto_apply,
    }
