import { useState, useEffect } from "react";
import axios from "axios"; // Axios 가져오기
import Header from "./components/Header";
import "./App.css";
import ItemList from "./components/ItemList";
import PharmacyList from "./components/PharmacyList";

const App = () => {
  const [selectedItem, setSelectedItem] = useState(null);
  const [searchTerm, setSearchTerm] = useState(""); // 검색어 상태 추가
  const [items, setItems] = useState([]); // DB에서 가져올 아이템 상태

  const pharmacys = [
    { id: 1, name: "가톨릭 약국", quantity: 600, prob: 89.9 },
    { id: 2, name: "약국2", quantity: 500, prob: 71.2 },
    { id: 3, name: "약국3", quantity: 300, prob: 98.3 },
  ];

  // 데이터베이스에서 아이템 가져오기
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/items/"); // Django API URL
        setItems(response.data); // 데이터 상태 업데이트
      } catch (error) {
        console.error("Error fetching items:", error);
      }
    };

    fetchItems();
  }, []); // 컴포넌트가 처음 렌더링될 때만 실행

  const handleItemClick = (item) => {
    setSelectedItem(item);
  };

  // 검색어에 따라 필터링된 데이터 생성
  const filteredItems = items.filter(
    (item) => item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-container">
      <Header
        onSearch={(term) => setSearchTerm(term)} // 검색어 상태 업데이트
      />
      <div className="horizontal-sections">
        <ItemList
          items={filteredItems} // 필터링된 아이템 전달
          selectedItem={selectedItem} // 선택된 아이템 전달
          onItemClick={handleItemClick} // 클릭 이벤트 전달
        />
        <PharmacyList selectedItem={selectedItem} pharmacys={pharmacys} />
      </div>
    </div>
  );
};

export default App;
