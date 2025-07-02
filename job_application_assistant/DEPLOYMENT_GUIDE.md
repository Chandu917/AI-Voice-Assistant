# Job Application Assistant - Deployment Guide

This guide covers how to deploy the Job Application Assistant system locally, using Docker, and on cloud platforms like Render.

---

## 1. Local Deployment

### Prerequisites

- Python 3.8+
- Node.js and npm
- Git

### Backend Setup

1. Navigate to the backend directory:

```bash
cd job_application_assistant/backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### Frontend Setup

1. Navigate to the frontend directory:

```bash
cd job_application_assistant/frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend development server:

```bash
npm start
```

4. Open your browser and visit:

```
http://localhost:3000
```

---

## 2. Docker Deployment

### Prerequisites

- Docker installed and running

### Build and Run Backend Docker Container

1. Create a `Dockerfile` in the backend directory with the following content:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Build the backend image:

```bash
docker build -t job-app-backend ./job_application_assistant/backend
```

3. Run the backend container:

```bash
docker run -d -p 8000:8000 --name job-app-backend job-app-backend
```

### Build and Run Frontend Docker Container

1. Create a `Dockerfile` in the frontend directory with the following content:

```dockerfile
FROM node:16-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

2. Build the frontend image:

```bash
docker build -t job-app-frontend ./job_application_assistant/frontend
```

3. Run the frontend container:

```bash
docker run -d -p 3000:3000 --name job-app-frontend job-app-frontend
```

4. Access the app at:

```
http://localhost:3000
```

---

## 3. Deployment on Render

1. Create two services on Render:

- **Backend Service:**
  - Connect your GitHub repo.
  - Set the root directory to `job_application_assistant/backend`.
  - Set the start command to:
    ```
    uvicorn main:app --host 0.0.0.0 --port 10000
    ```
  - Set environment variables as needed.
  - Expose port 10000.

- **Frontend Service:**
  - Connect your GitHub repo.
  - Set the root directory to `job_application_assistant/frontend`.
  - Set the start command to:
    ```
    npm start
    ```
  - Set environment variables if needed.
  - Expose port 3000.

2. Update frontend API URLs to point to the deployed backend URL.

---

## Notes

- Ensure CORS settings in backend allow requests from frontend domain.
- For production, consider building the frontend with `npm run build` and serving static files via a web server.
- Secure file uploads and validate inputs in production.

---

## Troubleshooting

- Check logs for errors.
- Verify ports are open and not blocked by firewall.
- Ensure environment variables are correctly set.

---

## Contact

For further assistance, please contact the development team.
