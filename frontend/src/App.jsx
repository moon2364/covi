import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [name, setName] = useState("None");
  const [quantity, setQuantity] = useState("None");
  const [prob, setProb] = useState("None");

  const clicked = () => {
    axios
      .get("http://127.0.0.1:8000", {
        params: {
          medicine: "타이레놀500mg 10T",
        },
      })
      .then((response) => {
        const data = response.data; // JSON 데이터를 객체로 가져옴
        setName(data.name); // 개별 상태 업데이트
        setQuantity(data.quantity);
        setProb(data.prob);
      })
      .catch((err) => {
        console.error("Error fetching data:", err);
      });
  };

  return (
    <div>
      <h1>약 정보</h1>
      <p>이름: {name}</p>
      <p>수량: {quantity}</p>
      <p>확률: {prob}</p>
      <button onClick={clicked}>클릭</button>
    </div>
  );
}

export default App;
