from controller.game_controller import GameController


if __name__ == "__main__":
    game_controller = GameController()
    game_controller.print_games()
    game_controller.launch_game_by_title(
        "The Elder Scrolls V: Skyrim Special Edition")
