import os

from model.game import Game
from model.library import Library
from view.game_viewer import GameViewer


class GameController:
    def __init__(self):
        self.__library = Library()

    def print_games(self):
        for game in self.__library.get_all_games():
            GameViewer.print_game(game)

    def launch_game(self, game: Game):
        os.startfile(game.path)

    def launch_game_by_title(self, title: str):
        found_game = self.__library.get_game_by_title(title)

        if found_game is not None:
            self.launch_game(found_game)
        else:
            GameViewer.game_not_found(title)

    def add_game(self, title, path, cover_art_path):
        self.__library.add_game(title, path, cover_art_path)

    def remove_game(self, title):
        self.__library.remove_game_by_title(title)
