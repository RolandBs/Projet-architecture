import React from "react";

export default function InputUrl({ url, setUrl }) {
  return (
    <div className="OuterContainer">
    <div className="Container">
      <label>
       <h2>YouTube URL:</h2>
        <input className="InputField" type="text" placeholder="Entrez votre url..." value={url} onChange={(e) => setUrl(e.target.value)} />
      </label>
      </div>
  </div>
  );
}
