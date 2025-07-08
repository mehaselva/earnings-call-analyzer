import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [ticker, setTicker] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState('');

  // Handle manual file selection
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setSummary('');
    setError('');
  };

  // Manual file upload + summarization
  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    setProgress(30);
    setError('');
    setSummary('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/analyze/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: (event) => {
          if (event.total) {
            const percent = Math.round((event.loaded / event.total) * 100);
            setProgress(percent);
          }
        },
      });

      setProgress(100);
      setSummary(response.data.summary);
    } catch (err) {
      setError('Upload failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Fetch from YouTube → trigger backend → summarize
  const handleFetchByTicker = async () => {
    if (!ticker.trim()) return;
    setLoading(true);
    setProgress(10);
    setError('');
    setSummary('');

    try {
      const fetchResponse = await axios.get(`http://127.0.0.1:8000/fetch-audio/?ticker=${ticker}`);
      setProgress(50);

      const filePath = fetchResponse.data.file_path;
      const analyzeResponse = await axios.post(
        'http://127.0.0.1:8000/analyze-from-path/',
        { file_path: filePath }
      );

      setProgress(100);
      setSummary(analyzeResponse.data.summary);
    } catch (err) {
      setError('Failed to fetch or analyze audio. Please try another ticker.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>AI-Powered Earnings Call Analyzer</h1>

      {/* Manual File Upload */}
      <div>
        <h3>Upload an MP3 File</h3>
        <input type="file" accept=".mp3" onChange={handleFileChange} />
        <button onClick={handleUpload} disabled={loading || !file}>
          Upload & Analyze
        </button>
      </div>

      <hr />

      {/* YouTube Fetch by Ticker */}
      <div>
        <h3>Or Fetch from YouTube</h3>
        <input
          type="text"
          placeholder="Enter Ticker (e.g., AAPL)"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
        />
        <button onClick={handleFetchByTicker} disabled={loading}>
          Fetch & Analyze
        </button>
      </div>

      {/* Progress Bar */}
      {loading && (
        <div style={{ marginTop: '20px' }}>
          <p>Processing... {progress}%</p>
          <div
            style={{
              width: '100%',
              height: '10px',
              backgroundColor: '#eee',
              borderRadius: '5px',
            }}
          >
            <div
              style={{
                width: `${progress}%`,
                height: '10px',
                backgroundColor: '#4caf50',
                borderRadius: '5px',
                transition: 'width 0.3s ease-in-out',
              }}
            ></div>
          </div>
        </div>
      )}

      {/* Error */}
      {error && (
        <div style={{ color: 'red', marginTop: '20px' }}>
          <p>{error}</p>
        </div>
      )}

      {/* Summary */}
      {summary && (
        <div style={{ marginTop: '20px' }}>
          <h2>LLM-Generated Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
