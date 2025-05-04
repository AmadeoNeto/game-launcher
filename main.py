from controller.game_controller import GameController


if __name__ == "__main__":
    game_controller = GameController()
    game_controller.add_game("The Elder Scrolls V: Skyrim Special Edition",
                             r"D:\SteamLibrary\steamapps\common\Skyrim Special Edition\SkyrimSELauncher.exe", r"assets/skyrim_se_cover.png")
    game_controller.print_games()
    game_controller.launch_game_by_title(
        "The Elder Scrolls V: Skyrim Special Edition")
    game_controller.remove_game("The Elder Scrolls V: Skyrim Special Edition")
