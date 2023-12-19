import React, { useState, useEffect } from 'react';

const AudioList = () => {
  const [audioFiles, setAudioFiles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/audio_files');
        const data = await response.json();
        setAudioFiles(data.audio_files);
      } catch (error) {
        console.error('Error fetching audio files:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Audio Files:</h2>
      <ul>
        {audioFiles.map((audioFile, index) => (
          <li key={index}>
            {audioFile}
            <audio controls>
              <source src={`http://localhost:8000/play_audio/${audioFile}`} type="audio/mp3" />
              Your browser does not support the audio element.
            </audio>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AudioList;
