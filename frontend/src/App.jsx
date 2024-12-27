import { useState } from 'react'
import axios from "axios";
import './App.css'

function App() {
  const [text, setText] = useState("None");
  
  const clicked = () => {
    axios
      .get("http://127.0.0.1:8000", {
        params: {
          medicine: "타이레놀500mg 10T",
        },
      })
      .then((response) => setText(JSON.stringify(response.data)));
  };

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={clicked}>클릭</button>
    </div>
  );
}

export default App;