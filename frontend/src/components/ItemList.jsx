/* eslint-disable react/prop-types */
// import React from "react";


const ItemList = ({ items, selectedItem, onItemClick }) => {
  return (
    <div className="section left-section">
      <h2 className="section-title">주문 예상 품목</h2>
      <hr />
      <p className="section-description">
        약국프로젝트 추천에 따라 주문이 예상되는 품목입니다. 주문 예상일
        전까지 사입을 완료해 주세요!
      </p>
      <table className="item-table">
        <thead>
          <tr>
            <th>품목</th>
            <th>예측 수량</th>
            <th>주문 예상 일자</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr
              key={item.id}
              className={selectedItem?.id === item.id ? "selected" : ""}
              onClick={() => onItemClick(item)} // 클릭 이벤트 실행
            >
              <td>{item.name}</td>
              <td>{item.quantity}</td>
              <td>{item.estimated_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ItemList;
