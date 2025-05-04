from model.game import Game


class GameViewer:
    @staticmethod
    def print_game(game: Game):
        print(game)

    @staticmethod
    def game_not_found(title: str):
        print(f"{title} was not found!")
