// src/components/FetchAudio.js
import React, { useState } from 'react';
import axios from 'axios';

function FetchAudio() {
  const [ticker, setTicker] = useState('');
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setTicker(e.target.value.toUpperCase()); // Always uppercase
  };

  const handleFetch = async () => {
    if (!ticker) return;

    setLoading(true);
    setStatus('');

    try {
      const response = await axios.get(`http://127.0.0.1:8000/fetch-audio?ticker=${ticker}`);
      setStatus(response.data.message || 'Audio fetched!');
    } catch (error) {
      setStatus(`Error: ${error.response?.data?.detail || 'Something went wrong'}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: '2rem' }}>
      <h2>Fetch Earnings Call by Ticker</h2>
      <input
        type="text"
        value={ticker}
        onChange={handleInputChange}
        placeholder="Enter Ticker Symbol (e.g. AAPL)"
      />
      <button onClick={handleFetch} disabled={loading}>
        {loading ? 'Fetching...' : 'Fetch Audio'}
      </button>
      {status && <p>{status}</p>}
    </div>
  );
}

export default FetchAudio;
