from dataclasses import dataclass
from datetime import datetime


@dataclass
class Game:
    game_id: int
    title: str
    path: str
    cover_art_path: str
    hours_played: float = 0
    last_played: datetime = None
