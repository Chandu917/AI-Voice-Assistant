# AI-Powered Job Application Assistant

This project is a full-stack AI-powered job application assistant that helps users manage their job search and automate applications.

## Features

- Web interface for profile management and job application tracking
- Secure backend with database storage for user profiles and documents
- Job scraping from multiple platforms (LinkedIn, Indeed, Naukri)
- AI-powered eligibility checking using Gemini or OpenAI
- Automated job application submission with Selenium
- Application status tracking and management

## Tech Stack

- Frontend: React
- Backend: FastAPI
- Database: SQLite (default, can be switched to MongoDB)
- Automation: Selenium with ChromeDriver
- AI Integration: Gemini or OpenAI API

## Setup

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install backend dependencies: `pip install -r requirements.txt`
4. Install frontend dependencies: `cd frontend && npm install`
5. Run backend: `uvicorn backend.main:app --reload`
6. Run frontend: `npm start` in the frontend directory
7. Configure ChromeDriver path and AI API keys in environment variables

## Folder Structure

- backend/
  - main.py
  - models.py
  - database.py
  - api/
    - profile.py
    - jobs.py
    - applications.py
  - services/
    - scraper.py
    - eligibility.py
    - automation.py
- frontend/
  - src/
    - components/
      - ProfileForm.jsx
      - JobList.jsx
      - ApplicationTracker.jsx
    - App.jsx
    - index.js
- scripts/
  - setup_chromedriver.sh

## Security

- User data and documents are stored securely with access controls.
- File uploads are sanitized and stored safely.
- API endpoints require authentication (to be implemented).

## Future Work

- Add user authentication and authorization
- Expand job platforms supported
- Improve AI eligibility model
- Deploy to cloud with HTTPS and domain
