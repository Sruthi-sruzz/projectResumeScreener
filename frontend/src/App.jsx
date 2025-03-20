import React, { useState } from "react";
import axios from "axios";

function App() {
  const [jobDescription, setJobDescription] = useState("");
  const [files, setFiles] = useState([]);
  const [results, setResults] = useState([]);

  const handleFileChange = (event) => {
    setFiles(event.target.files);
  };

  const handleUpload = async () => {
    if (files.length === 0) {
      alert("Please select resumes to upload.");
      return;
    }

    const formData = new FormData();
    for (let file of files) {
      formData.append("files", file);
    }

    try {
      const response = await axios.post("http://13.233.159.45:8000/upload-resumes/", formData);
      const uploadedFiles = response.data.results;
      
      const matchData = new FormData();
      matchData.append("job_description", jobDescription);
      uploadedFiles.forEach((filename) => matchData.append("filenames", filename));

      const matchResponse = await axios.post("http://13.233.159.45:8000/match-resumes/", matchData);
      setResults(matchResponse.data.results);
    } catch (error) {
      console.error("Error:", error);
      alert("Error uploading resumes.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Resume Screener</h1>
      <textarea
        placeholder="Enter Job Description"
        rows="4"
        cols="50"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />
      <br /><br />
      <input type="file" multiple onChange={handleFileChange} />
      <br /><br />
      <button onClick={handleUpload}>Upload & Get Scores</button>
      <h2>Results</h2>
      <ul>
        {results.map((result, index) => (
          <li key={index}>
            <strong>{result.filename}</strong> - Score: {result.match_score}%
            <br />
            <a href={result.file_url} target="_blank" rel="noopener noreferrer">View Resume</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

