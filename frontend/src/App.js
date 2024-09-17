import './App.css';
import React, { useState } from 'react';
import { ClipLoader } from 'react-spinners';

const App = () => {
  const [audioFile, setAudioFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  const handleFileChange = (event) => {
    setAudioFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!audioFile) return;

    const formData = new FormData();
    formData.append('file', audioFile);

    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch('http://127.0.0.1:8989/predict', {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json',
        },
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Error uploading audio file:', error);
      setResponse({ error: 'Error uploading audio file' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="Container">
      <h1 className="Title">Moroccan Music Classifier</h1>
      
      <label className="FileInput">
        <input type="file" accept="audio/*" onChange={handleFileChange} />
        {audioFile ? audioFile.name : "Upload an Audio File"}
      </label>

      <button className="UploadButton" onClick={handleUpload} disabled={!audioFile}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {loading && <ClipLoader color="#007bff" size={50} />}

      {response && (
        <div className="MessageContainer">
          {response.error ? (
            <h3>{response.error}</h3>
          ) : (
            <>
              <h3>Success!</h3>
              <p>The predicted class is: <br />
                <strong>{response.class}</strong></p>
            </>
          )}
        </div>
      )}
    </div>
  );
};


export default App;
