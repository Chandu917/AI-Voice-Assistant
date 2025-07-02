#!/bin/bash

# Test script for Job Application Assistant backend API endpoints

BASE_URL="http://localhost:8000/api"

echo "Testing Job Search API..."
curl -s -G "${BASE_URL}/jobs/search-jobs" --data-urlencode "query=Python Developer" --data-urlencode "date_posted=1w" | jq .

echo "Testing Apply Job API with valid job ID..."
curl -s -X POST "${BASE_URL}/applications/auto-apply" -H "Content-Type: application/json" -d '{"job_id":"1"}' | jq .

echo "Testing Apply Job API with invalid job ID..."
curl -s -X POST "${BASE_URL}/applications/auto-apply" -H "Content-Type: application/json" -d '{}' | jq .

echo "Testing Profile Creation API..."
curl -s -X POST "${BASE_URL}/profile/create" \
  -F "name=Test User" \
  -F "phone=1234567890" \
  -F "email=test@example.com" \
  -F "skills=Python,FastAPI,React" | jq .

echo "Testing Profile Retrieval API..."
curl -s "${BASE_URL}/profile/get" | jq .

echo "Testing Resume Upload API..."
curl -s -X POST "${BASE_URL}/upload/upload_resume" -F "file=@../test_resume.pdf" | jq .

echo "All tests completed."
