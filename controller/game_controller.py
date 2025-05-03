import os

from model.game import Game
from model.library import Library
from view.game_viewer import GameViewer


class GameController:
    def __init__(self):
        self.__library = Library()

        self.__library.add_game(Game(title="The Elder Scrolls V: Skyrim Special Edition",
                                     path="D:\SteamLibrary\steamapps\common\Skyrim Special Edition\SkyrimSELauncher.exe",
                                     cover_art_path="Assets\skyrim_se_cover.png"))

    def print_games(self):
        for game in self.__library.get_games():
            GameViewer.print_game(game)

    def launch_game(self, game: Game):
        os.startfile(game.path)

    def launch_game_by_title(self, title: str):
        found_game = self.__library.get_game_by_title(title)

        if found_game is not None:
            self.launch_game(found_game)
