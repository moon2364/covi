import { useState, useEffect } from "react";
import axios from "axios";
import Header from "./components/Header";
import "./App.css";
import ItemList from "./components/ItemList";
import PharmacyList from "./components/PharmacyList";

const App = () => {
  const [selectedItem, setSelectedItem] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [items, setItems] = useState([]);
  const [pharmacys, setPharmacys] = useState([]); // 약국 정보 상태

  // 데이터베이스에서 아이템 가져오기
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/buying-schedules/");
        setItems(response.data);
      } catch (error) {
        console.error("Error fetching items:", error);
      }
    };

    fetchItems();
  }, []);

  // 선택된 품목에 대한 약국 정보 가져오기
  useEffect(() => {
    const fetchPharmacys = async () => {
      if (selectedItem) {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/prediction-out/${selectedItem.id}/`
          );
          setPharmacys(response.data);
        } catch (error) {
          console.error("Error fetching pharmacy orders:", error);
          setPharmacys([]);
        }
      } else {
        setPharmacys([]);
      }
    };

    fetchPharmacys();
  }, [selectedItem]); // selectedItem이 변경될 때 실행

  const handleItemClick = (item) => {
    setSelectedItem(item);
  };

  const filteredItems = items.filter((item) =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-container">
      <Header onSearch={(term) => setSearchTerm(term)} />
      <div className="horizontal-sections">
        <ItemList
          items={filteredItems}
          selectedItem={selectedItem}
          onItemClick={handleItemClick}
        />
        <PharmacyList selectedItem={selectedItem} pharmacys={pharmacys} />
      </div>
    </div>
  );
};

export default App;
