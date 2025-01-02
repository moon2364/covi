/* eslint-disable react/prop-types */
// import React from "react";
// import "./PharmacyList.css";

const PharmacyList = ({ selectedItem, pharmacys }) => {
  return (
    <div className="section right-section">
      <h2 className="section-title">
        사입 스케줄
        <hr />
      </h2>
      <p className="section-description">
        {selectedItem ? (
          <>
            <strong style={{ fontSize: "1rem" }}>
              {selectedItem.medi_name}&nbsp;&nbsp;&nbsp;
            </strong>
            <strong style={{ fontSize: "0.8rem", opacity: "0.7" }}>
              총 예측 수량 : {selectedItem.prediction_qtt}
            </strong>
            <br />
            <table className="pharmacy-table">
              <thead>
                <tr>
                  <th>예상 약국</th>
                  <th>약국별 예상 수량</th>
                  <th>예상 날짜</th>
                  <th>주문 확률</th>
                </tr>
              </thead>
              <tbody>
                {pharmacys.map((item) => (
                  <tr key={item.id}>
                    <td>{item.prediction_pharm}</td>
                    <td>{item.pharm_per_qtt}</td>
                    <td>{item.prediction_dt}</td>
                    <td>{item.order_prob * 100}%</td>
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
