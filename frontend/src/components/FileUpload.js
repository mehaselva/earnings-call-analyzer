import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    console.log("Upload button clicked");  // ← debug log
    if (!file) {
        console.log("No file selected");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/analyze/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  return (
    <div>
      <h1>Upload MP3 for Analysis</h1>
      <input type="file" accept=".mp3" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {summary && (
        <div>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
