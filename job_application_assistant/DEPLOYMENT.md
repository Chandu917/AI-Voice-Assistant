# Deployment Guide for AI-Powered Job Application Assistant

## Prerequisites

- Python 3.11+
- Node.js 16+
- Chrome browser installed
- ChromeDriver matching your Chrome version (https://chromedriver.chromium.org/downloads)

## Backend Setup

1. Navigate to the backend directory:

```bash
cd job_application_assistant/backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn pydantic selenium
```

4. Set environment variables for AI API keys (Gemini/OpenAI):

```bash
export AI_API_KEY="your_api_key_here"
```

5. Run the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend Setup

1. Navigate to the frontend directory:

```bash
cd job_application_assistant/frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

The frontend will be available at http://localhost:3000

## Production Deployment

- Build the React app:

```bash
npm run build
```

- Serve the build folder with a static server or integrate with backend.

- Use a process manager like `pm2` or systemd to run the backend server.

- Configure HTTPS and domain as needed.

## Notes

- Ensure ChromeDriver is in your PATH or specify its location in your Selenium setup.

- Secure your AI API keys and user data.

- For cloud deployment, consider platforms like Render, Railway, or AWS.
