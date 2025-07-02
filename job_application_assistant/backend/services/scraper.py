import requests
from bs4 import BeautifulSoup
import time

def scrape_linkedin_jobs(keywords, location, max_results=20, max_pages=5, retry_attempts=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    jobs = []
    results_per_page = 25  # LinkedIn shows 25 jobs per page
    for page in range(max_pages):
        start = page * results_per_page
        url = f"https://www.linkedin.com/jobs/search?keywords={keywords}&location={location}&start={start}"
        attempts = 0
        while attempts < retry_attempts:
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                job_cards = soup.find_all("div", class_="result-card__contents")
                if not job_cards:
                    return jobs  # No more jobs
                for job_card in job_cards:
                    if len(jobs) >= max_results:
                        return jobs
                    title = job_card.find("h3", class_="result-card__title").text.strip()
                    company = job_card.find("h4", class_="result-card__subtitle").text.strip()
                    location_text = job_card.find("span", class_="job-result-card__location").text.strip()
                    link = job_card.find("a", class_="result-card__full-card-link")["href"]
                    job_entry = {
                        "title": title,
                        "company": company,
                        "location": location_text,
                        "link": link
                    }
                    if job_entry not in jobs:
                        jobs.append(job_entry)
                break  # Success, break retry loop
            except Exception as e:
                print(f"Error scraping LinkedIn jobs (attempt {attempts+1}): {e}")
                attempts += 1
                time.sleep(2)
        else:
            print("Max retries reached for LinkedIn scraping, moving on.")
            break
    return jobs

def scrape_indeed_jobs(keywords, location, max_results=20, max_pages=5, retry_attempts=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    jobs = []
    results_per_page = 10  # Indeed shows 10 jobs per page
    for page in range(max_pages):
        start = page * results_per_page
        url = f"https://www.indeed.com/jobs?q={keywords}&l={location}&start={start}"
        attempts = 0
        while attempts < retry_attempts:
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                job_cards = soup.find_all("div", class_="jobsearch-SerpJobCard")
                if not job_cards:
                    return jobs
                for job_card in job_cards:
                    if len(jobs) >= max_results:
                        return jobs
                    title = job_card.find("a", class_="jobtitle").text.strip()
                    company = job_card.find("span", class_="company").text.strip()
                    location_text = job_card.find("div", class_="location").text.strip() if job_card.find("div", class_="location") else ""
                    link = "https://www.indeed.com" + job_card.find("a", class_="jobtitle")["href"]
                    job_entry = {
                        "title": title,
                        "company": company,
                        "location": location_text,
                        "link": link
                    }
                    if job_entry not in jobs:
                        jobs.append(job_entry)
                break
            except Exception as e:
                print(f"Error scraping Indeed jobs (attempt {attempts+1}): {e}")
                attempts += 1
                time.sleep(2)
        else:
            print("Max retries reached for Indeed scraping, moving on.")
            break
    return jobs

def scrape_naukri_jobs(keywords, location, max_results=20, max_pages=5, retry_attempts=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    jobs = []
    results_per_page = 20  # Naukri shows 20 jobs per page
    for page in range(max_pages):
        start = page + 1  # Naukri pages start at 1
        url = f"https://www.naukri.com/{keywords}-jobs-in-{location}?page={start}"
        attempts = 0
        while attempts < retry_attempts:
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                job_cards = soup.find_all("article", class_="jobTuple")
                if not job_cards:
                    return jobs
                for job_card in job_cards:
                    if len(jobs) >= max_results:
                        return jobs
                    title = job_card.find("a", class_="title").text.strip()
                    company = job_card.find("a", class_="subTitle").text.strip()
                    location_text = job_card.find("li", class_="location").text.strip()
                    link = job_card.find("a", class_="title")["href"]
                    job_entry = {
                        "title": title,
                        "company": company,
                        "location": location_text,
                        "link": link
                    }
                    if job_entry not in jobs:
                        jobs.append(job_entry)
                break
            except Exception as e:
                print(f"Error scraping Naukri jobs (attempt {attempts+1}): {e}")
                attempts += 1
                time.sleep(2)
        else:
            print("Max retries reached for Naukri scraping, moving on.")
            break
    return jobs
