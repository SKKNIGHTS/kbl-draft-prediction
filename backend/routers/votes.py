from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Vote
from schemas import VoteInput

router = APIRouter(prefix="/votes", tags=["Votes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def submit_vote(vote: VoteInput, db: Session = Depends(get_db)):
    new_vote = Vote(user_name=vote.user_name, player_id=vote.player_id, rank=vote.rank)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return {"status": "success"}

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    result = db.execute("""
        SELECT p.name, AVG(v.rank) as avg_rank, COUNT(v.id) as votes
        FROM votes v JOIN players p ON v.player_id = p.id
        GROUP BY p.name
        ORDER BY avg_rank ASC
    """).fetchall()
    return [{"name": r[0], "avg_rank": r[1], "votes": r[2]} for r in result]
