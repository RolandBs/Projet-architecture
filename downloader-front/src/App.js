import React, { useState } from 'react';
import './App.css';
// "proxy": "http://localhost:8000",

function App() {
  const [url, setUrl] = useState('');
  const [videoName, setVideoName] = useState('');
  const [formatChoice, setFormatChoice] = useState('opus');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:8000/api/download/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        url,
        video_name: videoName,
        format_choice: formatChoice,
      }),
    });
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          YouTube URL:
          <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} />
        </label>
        <br />
        <label>
          Video Name:
          <input type="text" value={videoName} onChange={(e) => setVideoName(e.target.value)} />
        </label>
        <br />
        <label>
          Format:c
          <select value={formatChoice} onChange={(e) => setFormatChoice(e.target.value)}>
            <option value="mp3">MP3</option>
            <option value="opus">Opus</option>
            <option value="flac">Flac</option>
            <option value="vorbis">Vorbis</option>
          </select>
        </label>
        <br />
        <button type="submit">Download</button>
      </form>
    </div>
  );
}

export default App;
