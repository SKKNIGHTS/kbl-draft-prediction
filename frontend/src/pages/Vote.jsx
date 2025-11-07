import { useEffect, useState } from "react";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import { useNavigate } from "react-router-dom";
import api from "../api";
import "./Vote.css";

export default function Vote() {
  const [players, setPlayers] = useState([]);
  const [teams, setTeams] = useState({
    "정관장": [],
    "DB": [],
    "KCC": [],
    "소노": [],
    "삼성": [],
    "가스공사": [],
    "모비스": [],
    "KT": [],
    "SK": [],
    "LG": [],
  });

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

    // 동일 칸 내 이동
    if (source.droppableId === destination.droppableId) return;

    const copyPlayers = Array.from(players);
    const copyTeams = JSON.parse(JSON.stringify(teams));

    // 선수 정보 추출
    const [moved] = source.droppableId === "players"
      ? copyPlayers.splice(source.index, 1)
      : copyTeams[source.droppableId].splice(source.index, 1);

    // 대상 칸으로 이동 (한 칸당 1명만)
    if (destination.droppableId === "players") {
      copyPlayers.splice(destination.index, 0, moved);
    } else {
      if (copyTeams[destination.droppableId].length >= 1) {
        alert("이 팀에는 이미 선수가 있습니다!");
        return;
      }
      copyTeams[destination.droppableId].splice(destination.index, 0, moved);
    }

    setPlayers(copyPlayers);
    setTeams(copyTeams);
  };

  const handleSubmit = async () => {
    const selected = Object.entries(teams)
      .map(([team, players]) => ({
        team,
        player: players[0] || null,
      }))
      .filter((item) => item.player);

    if (selected.length < Object.keys(teams).length) {
      alert("모든 팀에 선수를 배치해주세요!");
      return;
    }

    try {
      const votes = selected.map((entry, i) => ({
        user_name: username,
        player_id: entry.player.id,
        rank: i + 1,
      }));

      await api.post("/votes/bulk", { user_name: username, votes });
      alert("✅ 팀별 예측 완료! 감사합니다 🙌");
      navigate("/result");
    } catch (err) {
      console.error("❌ 투표 저장 실패:", err.response?.data || err.message || err);
      alert("저장 중 오류가 발생했습니다.");
    }
  };

  const handleReset = () => {
    if (window.confirm("모든 팀 예측을 초기화할까요?")) {
      setTeams({
        "정관장": [],
        "DB": [],
        "KCC": [],
        "소노": [],
        "삼성": [],
        "가스공사": [],
        "모비스": [],
        "KT": [],
        "SK": [],
        "LG": [],
      });
    }
  };

  const handleResult = () => {
    navigate("/result");
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

        {/* 오른쪽: 팀별 드래프트 칸 */}
        <div className="teams-column">
          <h2>팀별 순서 예측</h2>
          {Object.keys(teams).map((team, tIndex) => (
            <Droppable droppableId={team} key={team}>
              {(provided) => (
                <div
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                  className="team-slot"
                >
                  <div className="team-label">{`${tIndex + 1}. ${team}`}</div>
                  {teams[team].length === 0 ? (
                    <div className="empty-slot">선수 드래그 →</div>
                  ) : (
                    teams[team].map((p, index) => (
                      <Draggable
                        key={p.id}
                        draggableId={`${team}-${p.id}`}
                        index={index}
                      >
                        {(prov) => (
                          <div
                            ref={prov.innerRef}
                            {...prov.draggableProps}
                            {...prov.dragHandleProps}
                            className="team-player"
                          >
                            <span>{p.name}</span>
                            <span className="team-school">{p.school}</span>
                          </div>
                        )}
                      </Draggable>
                    ))
                  )}
                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          ))}

          <div className="vote-controls">
            <button onClick={handleSubmit} className="submit-btn">
              제출하기
            </button>
            <button onClick={handleReset} className="reset-btn">
              초기화
            </button>
            <button onClick={handleResult} className="submit-btn">
              결과보기
            </button>
          </div>
        </div>
      </DragDropContext>
    </div>
  );
}
