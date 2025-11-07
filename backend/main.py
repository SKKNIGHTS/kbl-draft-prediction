from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from collections import Counter
from fastapi.responses import JSONResponse
from routers import players

app = FastAPI(title="KBL Draft API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players.router)

@app.get("/")
def root():
    return {"message": "Server running ✅"}


# ✅ Vote 데이터 구조
class Vote(BaseModel):
    user_name: str
    player_id: int
    rank: int

class VoteBulk(BaseModel):
    user_name: str
    votes: List[Vote]

# ✅ 메모리 기반 저장소
votes_db: List[Vote] = []


@app.post("/votes/")
def create_vote(vote: Vote):
    """
    같은 user_name으로 이미 투표한 항목이 있으면 기존 데이터 삭제 후 새로 저장.
    """
    # 기존 사용자 투표 제거
    global votes_db
    votes_db = [v for v in votes_db if v.user_name != vote.user_name]

    # 같은 이름으로 들어온 새 투표는 리스트에 추가
    votes_db.append(vote)

    print(f"✅ {vote.user_name}의 새 투표 저장: player_id={vote.player_id}, rank={vote.rank}")
    return {"message": f"{vote.user_name}님의 투표가 갱신되었습니다."}


@app.get("/votes/")
def list_votes():
    return votes_db


@app.get("/votes/summary")
def get_vote_summary():
    if not votes_db:
        return JSONResponse(
            content={"message": "아직 투표가 없습니다."},
            media_type="application/json; charset=utf-8"
        )

    player_counts = Counter([vote.player_id for vote in votes_db])
    sorted_players = sorted(player_counts.items(), key=lambda x: x[1], reverse=True)

    top10 = [
        {"player_id": pid, "votes": count}
        for pid, count in sorted_players[:10]
    ]

    return JSONResponse(
        content={"total_votes": len(votes_db), "top10": top10},
        media_type="application/json; charset=utf-8"
    )

# ✅ 전체 투표 데이터 초기화 기능
@app.delete("/votes/reset")
def reset_votes():
    """모든 투표 기록을 삭제"""
    global votes_db
    count = len(votes_db)
    votes_db.clear()
    print(f"🗑️ 전체 투표 {count}개 삭제 완료")
    return {"message": f"전체 투표 {count}개가 삭제되었습니다."}

@app.delete("/votes/{username}")
def delete_user_votes(username: str):
    """특정 유저의 투표 삭제"""
    global votes_db
    before = len(votes_db)
    votes_db = [v for v in votes_db if v.user_name != username]
    after = len(votes_db)
    deleted = before - after
    print(f"🗑️ {username}의 투표 {deleted}개 삭제 완료")
    return {"message": f"{username}의 투표 {deleted}개가 삭제되었습니다."}

@app.post("/votes/bulk")
def create_bulk_vote(data: VoteBulk):
    """
    같은 유저의 여러 순위 투표를 한 번에 저장 (덮어쓰기)
    """
    global votes_db
    # 기존 유저 투표 삭제
    votes_db = [v for v in votes_db if v.user_name != data.user_name]

    # 새 투표 전체 추가
    for v in data.votes:
        votes_db.append(v)

    print(f"✅ {data.user_name}의 투표 {len(data.votes)}개 저장 완료")
    return {"message": f"{data.user_name}의 투표 {len(data.votes)}개가 저장되었습니다."}