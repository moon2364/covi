import { useState } from "react";
import "./Header.css";

// eslint-disable-next-line react/prop-types
const Header = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleInputChange = (e) => {
    const term = e.target.value;
    setSearchTerm(term);
    onSearch(term); // 검색어를 부모 컴포넌트로 전달
  };

  return (
    <header className="header">
      <div className="search-container">
        <input
          type="text"
          className="search-input"
          placeholder="품목 검색..."
          value={searchTerm}
          onChange={handleInputChange}
        />
        <button className="search-button">🔍</button>
        <button className="filter-button">필터</button>
      </div>
    </header>
  );
};

export default Header;
