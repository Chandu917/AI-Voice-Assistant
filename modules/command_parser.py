import re

def parse_job_application_command(command_text):
    """
    Parses natural language job commands.
    Returns extracted parameters:
    - job_title
    - locations
    - companies
    - remote_only (bool)
    - eligibility_threshold (float)
    - auto_apply (bool)
    """
    command_text = command_text.lower()

    # Improved regex to handle more flexible phrasing and optional words
    job_title_match = re.search(
        r"(?:apply for|search(?:ing)?|find|look for|apply to|apply)\s+(.*?)\s+(?:jobs|roles|positions|openings|vacancies)?",
        command_text
    )
    job_title = job_title_match.group(1).strip() if job_title_match else None

    # Find all locations mentioned after "in" or "at"
    locations = re.findall(r"(?:in|at) ([a-z\s]+)", command_text)

    # Find all companies mentioned after "company" or "at"
    companies = re.findall(r"(?:company|at) ([a-z\s,]+)", command_text)
    companies_list = []
    if companies:
        # Split by comma and strip whitespace
        companies_list = [c.strip() for c in companies[0].split(",")]

    remote_only = "remote" in command_text

    eligibility_threshold = 1.0
    threshold_match = re.search(r"meet (\d+)%", command_text)
    if threshold_match:
        eligibility_threshold = float(threshold_match.group(1)) / 100.0

    auto_apply = not ("confirm" in command_text or "wait for" in command_text)

    return {
        "job_title": job_title,
        "locations": locations,
        "companies": companies_list,
        "remote_only": remote_only,
        "eligibility_threshold": eligibility_threshold,
        "auto_apply": auto_apply
    }
