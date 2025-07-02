import React from 'react';

const JobList = ({ jobs }) => {
  if (!jobs || jobs.length === 0) {
    return <p>No jobs found.</p>;
  }

  return (
    <div>
      <h2>Job Listings</h2>
      <ul>
        {jobs.map((job, index) => (
          <li key={index} style={{ marginBottom: '1rem' }}>
            <strong>📌 {job.title}</strong> at <em>{job.company}</em><br />
            🌐 {job.location}<br />
            🗓️ Posted: {job.date_posted || 'N/A'}<br />
            🔗 <a href={job.link} target="_blank" rel="noopener noreferrer">Job Link</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JobList;
