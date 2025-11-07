from pydantic import BaseModel

class VoteInput(BaseModel):
    user_name: str
    player_id: int
    rank: int

class PlayerOutput(BaseModel):
    id: int
    name: str
    position: str
    team: str

    class Config:
        from_attributes = True
