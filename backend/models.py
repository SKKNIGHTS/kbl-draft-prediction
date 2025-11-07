from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from database import Base
from datetime import datetime

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    position = Column(String)
    team = Column(String)

class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    player_id = Column(Integer, ForeignKey("players.id"))
    rank = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)
