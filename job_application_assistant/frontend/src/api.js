const API_URL = "http://localhost:8000/api";

export async function fetchJobs(role, location, dateRange) {
  // The backend jobs search endpoint is /api/jobs/search-jobs with query parameter 'query' for role
  const response = await fetch(`${API_URL}/jobs/search-jobs?query=${encodeURIComponent(role)}&date_posted=${encodeURIComponent(dateRange)}&remote=true`);
  return await response.json();
}

export async function applyJob(jobId) {
  // The backend applications auto-apply endpoint is /api/applications/auto-apply
  const response = await fetch(`${API_URL}/applications/auto-apply`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ job_id: jobId }),
  });
  return await response.json();
}

export async function uploadResume(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:8000/api/upload/upload_resume", {
    method: "POST",
    body: formData,
  });
  return await response.json();
}
