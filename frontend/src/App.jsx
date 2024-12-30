import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [medicine, setMedicine] = useState({
    name: "None",
    quantity: "None",
    prob: "None",
  });
  
  const clicked = () => {
    axios
      .get("http://127.0.0.1:8000", {
        params: {
          medicine: "타이레놀500mg 10T",
        },
      })
      .then((response) => {
        const data = response.data;
        setMedicine({
          name: data.name,
          quantity: data.quantity,
          prob: data.prob,
        });
      })
      .catch((err) => {
        console.error("Error fetching data:", err);
      });
  };
  

  return (
    <div>
      <h1>약 정보</h1>
      <p>이름: {medicine.name}</p>
      <p>수량: {medicine.quantity}</p>
      <p>확률: {medicine.prob}</p>
      <button onClick={clicked}>클릭</button>
    </div>
  );
}

export default App;
