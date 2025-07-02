import React, { useState, useEffect } from "react";

const ProfileForm = () => {
  const [profile, setProfile] = useState({
    name: "",
    phone: "",
    email: "",
    linkedin: "",
    github: "",
    skills: "",
    experience: "",
    jobPreferences: "",
    resume: null,
    coverLetter: null,
    certificates: null,
  });

  useEffect(() => {
    // Fetch existing profile data
    fetch("http://localhost:8000/api/profile/get")
      .then((res) => res.json())
      .then((data) => {
        if (!data.message) {
          setProfile({
            ...profile,
            ...data,
            skills: data.skills ? data.skills.join(",") : "",
            jobPreferences: JSON.stringify(data.job_preferences || {}, null, 2),
          });
        }
      });
  }, []);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (files) {
      setProfile({ ...profile, [name]: files[0] });
    } else {
      setProfile({ ...profile, [name]: value });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    for (const key in profile) {
      if (profile[key]) {
        formData.append(key, profile[key]);
      }
    }
    fetch("http://localhost:8000/api/profile/create", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        alert("Profile saved successfully!");
      })
      .catch((err) => {
        alert("Error saving profile.");
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Profile Information</h2>
      <label>Name:</label>
      <input type="text" name="name" value={profile.name} onChange={handleChange} required />
      <label>Phone:</label>
      <input type="text" name="phone" value={profile.phone} onChange={handleChange} required />
      <label>Email:</label>
      <input type="email" name="email" value={profile.email} onChange={handleChange} required />
      <label>LinkedIn:</label>
      <input type="text" name="linkedin" value={profile.linkedin} onChange={handleChange} />
      <label>GitHub:</label>
      <input type="text" name="github" value={profile.github} onChange={handleChange} />
      <label>Skills (comma separated):</label>
      <input type="text" name="skills" value={profile.skills} onChange={handleChange} />
      <label>Experience:</label>
      <textarea name="experience" value={profile.experience} onChange={handleChange} />
      <label>Job Preferences (JSON):</label>
      <textarea name="jobPreferences" value={profile.jobPreferences} onChange={handleChange} />
      <label>Resume (PDF):</label>
      <input type="file" name="resume" accept=".pdf" onChange={handleChange} />
      <label>Cover Letter (PDF):</label>
      <input type="file" name="coverLetter" accept=".pdf" onChange={handleChange} />
      <label>Certificates (PDF):</label>
      <input type="file" name="certificates" accept=".pdf" onChange={handleChange} />
      <button type="submit">Save Profile</button>
    </form>
  );
};

export default ProfileForm;
