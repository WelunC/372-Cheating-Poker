from game_manager import GameManager  # Ensure the correct path for GameManager import

if __name__ == "__main__":
    game_manager = GameManager()
    selected_game_type = game_manager.select_game_type()  # Select game type before AI difficulty
    game_manager.play_game(selected_game_type)
