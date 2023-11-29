import React from "react";

export default function FormatSelector({formatChoice, setFormatChoice}) {
  return (
    <div className="OuterContainer">
      <div className="Container">
        <label>
          <h2 className="SubTitle">Format :</h2>
          <select 
            className="SelectField"
            value={formatChoice}
            onChange={(e) => setFormatChoice(e.target.value)}
          >
            <option value="mp3">MP3</option>
            <option value="opus">Opus</option>
            <option value="flac">Flac</option>
            <option value="vorbis">Vorbis</option>
          </select>
        </label>
      </div>
    </div>
  );
}
