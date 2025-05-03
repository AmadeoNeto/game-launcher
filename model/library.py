from dataclasses import dataclass
from typing import List
from model.game import Game


class Library:
    def __init__(self):
        self.__games: list[Game] = []

    def get_games(self) -> List[Game]:
        return self.__games

    def add_game(self, game: Game):
        self.__games.append(game)

    def remove_game(self, game: Game):
        self.__games.remove(game)

    def get_game_by_title(self, title: str) -> Game | None:
        found_game = None

        for game in self.__games:
            if game.title == title:
                found_game = game
                break

        return found_game
