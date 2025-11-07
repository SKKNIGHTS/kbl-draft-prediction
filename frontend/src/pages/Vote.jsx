import { useEffect, useState } from "react";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import { useNavigate } from "react-router-dom";
import api from "../api";
import "./Vote.css";

export default function Vote() {
  const [players, setPlayers] = useState([]);
  const [top10, setTop10] = useState([]);
  const navigate = useNavigate();
  const username = localStorage.getItem("username");

  useEffect(() => {
    if (!username) navigate("/");
    api
      .get("/players/")
      .then((res) => setPlayers(res.data))
      .catch((err) => console.error("❌ 선수 목록 로드 실패:", err));
  }, [navigate, username]);

  const onDragEnd = (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const copyPlayers = Array.from(players);
    const copyTop10 = Array.from(top10);

    if (source.droppableId === destination.droppableId) {
      const items =
        source.droppableId === "players" ? copyPlayers : copyTop10;
      const [moved] = items.splice(source.index, 1);
      items.splice(destination.index, 0, moved);
      if (source.droppableId === "players") setPlayers(items);
      else setTop10(items);
    } else {
      const [moved] =
        source.droppableId === "players"
          ? copyPlayers.splice(source.index, 1)
          : copyTop10.splice(source.index, 1);

      if (destination.droppableId === "players") {
        copyPlayers.splice(destination.index, 0, moved);
      } else {
        if (copyTop10.length >= 10) {
          alert("10명까지만 선택할 수 있습니다!");
          return;
        }
        copyTop10.splice(destination.index, 0, moved);
      }
      setPlayers(copyPlayers);
      setTop10(copyTop10);
    }
  };

  const handleSubmit = async () => {
    if (top10.length < 10) {
      alert("10명을 모두 채워주세요!");
      return;
    }

    try {
      const votes = top10.map((p, i) => ({
        user_name: username,
        player_id: p.id,
        rank: i + 1,
      }));

      await api.post("/votes/bulk", {
        user_name: username,
        votes: votes,
      });

      alert("✅ 투표 완료! 감사합니다 🙌");
      navigate("/result");
    } catch (err) {
      console.error("❌ 투표 저장 실패:", err);
      alert("저장 중 오류가 발생했습니다.");
    }
  };

  const handleReset = () => {
    if (window.confirm("순위 예측을 모두 초기화할까요?")) {
      setTop10([]);
    }
  };

  return (
    <div className="vote-container">
      <DragDropContext onDragEnd={onDragEnd}>
        {/* 왼쪽: 전체 선수 목록 */}
        <Droppable droppableId="players">
          {(provided) => (
            <div
              ref={provided.innerRef}
              {...provided.droppableProps}
              className="vote-column"
            >
              <h2>전체 선수 목록</h2>
              {players.map((p, index) => (
                <Draggable key={p.id} draggableId={p.id.toString()} index={index}>
                  {(prov) => (
                    <div
                      ref={prov.innerRef}
                      {...prov.draggableProps}
                      {...prov.dragHandleProps}
                      className="player-card"
                    >
                      <div className="player-info">
                        <span className="player-name">{p.name}</span>
                        <span className="player-pos">{p.position}</span>
                      </div>
                      <div className="player-school">{p.school}</div>
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>

        {/* 오른쪽: 나의 순위 예측 */}
        <Droppable droppableId="top10">
          {(provided) => (
            <div
              ref={provided.innerRef}
              {...provided.droppableProps}
              className="vote-column"
            >
              <h2>나의 순위 예측</h2>
              {top10.length === 0 && (
                <p className="empty">왼쪽에서 드래그하여 추가</p>
              )}
              {top10.map((p, index) => (
                <Draggable key={p.id} draggableId={p.id.toString()} index={index}>
                  {(prov) => (
                    <div
                      ref={prov.innerRef}
                      {...prov.draggableProps}
                      {...prov.dragHandleProps}
                      className="rank-card"
                    >
                      <span className="rank-number">{index + 1}위</span>
                      <div className="rank-info">
                        <span className="rank-name">{p.name}</span>
                        <span className="rank-school">{p.school}</span>
                      </div>
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
              <div className="vote-controls">
                <button onClick={handleSubmit} className="submit-btn">
                  제출하기
                </button>
                <button onClick={handleReset} className="reset-btn">
                  초기화
                </button>
              </div>
            </div>
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
}
