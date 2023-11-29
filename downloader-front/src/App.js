import React, { useState } from "react";
import "./App.css";
import InputUrl from "./Composant/InputUrl";
import NameVideo from "./Composant/NameVideo";
import FormatSelector from "./Composant/FormatSelector";
// "proxy": "http://localhost:8000",

function App() {
  const [url, setUrl] = useState('');
  const [videoName, setVideoName] = useState('');
  const [installPath, setInstallPath] = useState('');
  const [formatChoice, setFormatChoice] = useState('opus');


 const handleSubmit = async (e) => {
    e.preventDefault();

    const selectedPath = window.prompt('Specify installation path:', installPath);
    setInstallPath(selectedPath);

    const response = await fetch('http://localhost:8000/api/download/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          url,
          video_name: videoName,
          format_choice: formatChoice,
          install_path: selectedPath,

        }),
      });
  };

  return (
    <div className="App">
      <div className="Title">
        <h1>Pydoyt</h1>
      </div>
      <main className="FlexContainer">
        <form onSubmit={handleSubmit}>
          <InputUrl url={url} setUrl={setUrl} />
          <FormatSelector formatChoice={formatChoice} setFormatChoice={setFormatChoice}  />
          <button type="submit" className="DownloadButton">Télécharger</button>
        </form>
      </main>
    </div>
  );
}

export default App;
