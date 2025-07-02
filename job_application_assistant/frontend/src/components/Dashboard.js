import React, { useEffect, useState } from "react";
import { fetchJobs, applyJob, uploadResume } from "../api";

function Dashboard() {
  const [jobs, setJobs] = useState([]);
  const [file, setFile] = useState(null);

  useEffect(() => {
    fetchJobs("Python Developer", "Remote", "1week").then(data => {
      // Defensive check for data.jobs
      if (data && Array.isArray(data)) {
        setJobs(data);
      } else if (data && data.jobs && Array.isArray(data.jobs)) {
        setJobs(data.jobs);
      } else {
        setJobs([]);
      }
    });
  }, []);

  const handleApply = (jobId) => {
    applyJob(jobId).then(res => alert(res.status));
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (file) {
      uploadResume(file).then(res => alert(res.status));
    }
  };

  return (
    <div>
      <h1>Job Dashboard</h1>

      <div>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload Resume</button>
      </div>

      {jobs.map(job => (
        <div key={job.id} style={{ border: "1px solid gray", padding: "10px", margin: "10px" }}>
          <h3>{job.title}</h3>
          <p>{job.company} - {job.location}</p>
          <a href={job.link} target="_blank" rel="noopener noreferrer">Job Link</a><br/>
          <button onClick={() => handleApply(job.id)}>Apply</button>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;
