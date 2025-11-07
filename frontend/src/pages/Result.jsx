import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import "./Result.css";

export default function Result() {
  const [votes, setVotes] = useState([]);
  const [players, setPlayers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [error, setError] = useState(null);
  const username = localStorage.getItem("username");
  const navigate = useNavigate();

  // 데이터 불러오기
  const loadData = () => {
    Promise.all([api.get("/votes/"), api.get("/players/")])
      .then(([voteRes, playerRes]) => {
        setVotes(voteRes.data);
        setPlayers(playerRes.data);
      })
      .catch((err) => {
        console.error("❌ 데이터 로드 실패:", err);
        setError("데이터를 불러올 수 없습니다.");
      });
  };

  useEffect(() => {
    loadData();
  }, []);

  // 🔥 개별 유저 투표 삭제
  const handleDeleteUser = async (user) => {
    if (!window.confirm(`${user}님의 투표를 정말 삭제할까요?`)) return;
    try {
      await api.delete(`/votes/${user}`);
      alert(`${user}님의 투표가 삭제되었습니다.`);
      loadData(); // 즉시 새로고침
    } catch (err) {
      console.error("❌ 삭제 실패:", err);
      alert("삭제 중 오류가 발생했습니다.");
    }
  };

  const handleGoLogin = () => {
     navigate("/"); // ✅ Login 페이지로 이동
   };

  if (error) {
    return <div style={{ padding: 20, color: "red" }}>{error}</div>;
  }

  if (!votes.length || !players.length) {
    return <div style={{ padding: 20 }}>📡 데이터를 불러오는 중...</div>;
  }

  const uniqueUsers = [...new Set(votes.map((v) => v.user_name))];

  const getUserVotes = (user) => {
    return votes
      .filter((v) => v.user_name === user)
      .sort((a, b) => a.rank - b.rank)
      .map((v) => {
        const player = players.find((p) => p.id === v.player_id);
        return {
          ...v,
          player_name: player ? player.name : `#${v.player_id}`,
        };
      });
  };

  return (
    <div className="result-container">
      <h1 className="result-title">🏀 전체 투표 기록 🏀</h1>

      <p>총 투표자 수: {uniqueUsers.length}</p>

      <div className="user-list">
        {uniqueUsers.map((user) => (
          <div key={user} className="user-block">
            <div className="user-header">
              <button
                className={`user-button ${
                  selectedUser === user ? "active" : ""
                }`}
                onClick={() =>
                  setSelectedUser(selectedUser === user ? null : user)
                }
              >
                {user}
              </button>

              {username === "관리자" && (
                <button
                  className="delete-btn"
                  onClick={() => handleDeleteUser(user)}
                >
                  🗑
                </button>
              )}
            </div>

            {selectedUser === user && (
              <table className="result-table">
                <thead>
                  <tr>
                    <th>순위</th>
                    <th>선수 이름</th>
                  </tr>
                </thead>
                <tbody>
                  {getUserVotes(user).map((vote, idx) => (
                    <tr key={idx}>
                      <td>{vote.rank}</td>
                      <td>{vote.player_name}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        ))}
      </div>
      <div className="bottom-btn-container">
        <button onClick={handleGoLogin} className="go-login-btn">
        ← 로그인으로 돌아가기
        </button>
      </div>
    </div>
  );
}
