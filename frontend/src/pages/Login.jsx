import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // ✅ 기존 스타일 유지

export default function Login() {
  const [name, setName] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (!name.trim()) {
      alert("이름을 입력해주세요!");
      return;
    }
    localStorage.setItem("username", name.trim());
    navigate("/vote");
  };

  const handleGoResult = () => {
    navigate("/result");
  };

  return (
    <div className="login-container">
      <h1 className="login-title">🏀 YSAL 농구팀배 KBL 드래프트 예측 🏀</h1>

      <input
        className="login-input"
        placeholder="이름을 입력하세요"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <button onClick={handleLogin} className="login-button">
        시작하기
      </button>

      {/* ✅ 결과 페이지 이동 버튼 추가 */}
      <button onClick={handleGoResult} className="login-button">
        결과 보기
      </button>
    </div>
  );
}
