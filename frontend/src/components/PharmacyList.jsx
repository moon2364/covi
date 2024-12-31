/* eslint-disable react/prop-types */
// import React from "react";
// import "./PharmacyList.css";

const PharmacyList = ({ selectedItem, pharmacys }) => {
  return (
    <div className="section right-section">
      <h2 className="section-title">
        주문 예상 약국
        <hr />
      </h2>
      <p className="section-description">
        {selectedItem ? (
          <>
            <strong style={{ fontSize: "1rem" }}>
              {selectedItem.name}&nbsp;&nbsp;&nbsp;
            </strong>
            <strong style={{ fontSize: "0.8rem", opacity: "0.7" }}>
              총 수량 : {selectedItem.quantity}
            </strong>
            <br />
            <table className="pharmacy-table">
              <thead>
                <tr>
                  <th>주문 예상 약국</th>
                  <th>재고 수량</th>
                  <th>단가</th>
                </tr>
              </thead>
              <tbody>
                {pharmacys.map((item) => (
                  <tr key={item.id}>
                    <td>{item.name}</td>
                    <td>{item.quantity}</td>
                    <td>{item.unit_price}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
        ) : (
          "좌측에서 품목을 선택해주세요."
        )}
      </p>
    </div>
  );
};

export default PharmacyList;