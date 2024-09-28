from pydantic import BaseModel


class LeaderboardResponse(BaseModel):
    id: int
    username: str
    coins: int
