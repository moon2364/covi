/* eslint-disable react/prop-types */
// import React from "react";

const ItemList = ({ items, selectedItem, onItemClick }) => {
  return (
    <div className="section left-section">
      <h2 className="section-title">예측 결과 품목</h2>
      <hr />
      <p className="section-description">
        약국 프로젝트에서 예측한 주문 예상 품목입니다. 품목을 선택하여 상세 정보를 확인하세요.
      </p>
      <table className="item-table">
        <thead>
          <tr>
            <th>품목</th>
            <th>예측 수량</th>
            <th>재고</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr
              key={item.prediction_no}
              className={selectedItem?.prediction_no === item.prediction_no ? "selected" : ""}
              onClick={() => onItemClick(item)} // 클릭 이벤트 실행
            >
              <td>{item.medi_name}</td>
              <td>{item.prediction_qtt}</td>
              <td>{item.amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ItemList;
