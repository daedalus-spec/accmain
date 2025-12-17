import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

function Dashboard() {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const username = params.get("user");

  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // later connect to backend API
    // example: fetch("http://localhost:5000/user/" + username)
    // for now use dummy data

    const dummy = {
      name: username,
      accountNumber: "9876543210",
      balance: "₹ 45,000"
    };

    setUserData(dummy);
  }, [username]);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Welcome, {username}</h2>

      {userData && (
        <div style={{ marginTop: "20px" }}>
          <p><strong>Account Number:</strong> {userData.accountNumber}</p>
          <p><strong>Balance:</strong> {userData.balance}</p>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
