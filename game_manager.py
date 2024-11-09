from card_deck import Deck
from player import Player
from five_card_draw import FiveCardDrawGame  # Import the specific game class
from cheat_manager import CheatManager



class GameManager:
    def __init__(self):
        self.deck = Deck(num_decks=6)
        self.players = [Player("Human", is_human=True)]
        self.ai_difficulty = None
        self.cheat_manager = None
        self.games_played = 0
        self.games_won = 0

    def select_game_type(self):
        while True:
            return "five_card_draw"

    def select_ai_difficulty(self):
        while True:
            print("\nSelect AI difficulty:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Debug (Cheats fully allowed)")
            choice = input("Enter your choice (1, 2, 3 or 4): ")
            if choice == '1':
                return "easy"
            elif choice == '2':
                return "medium"
            elif choice == '3':
                return "hard"
            elif choice == '4':
                return "debug"
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

    def end_game_options(self):
        while True:
            choice = input("\nChoose an option: 'Play again' or 'Quit' ").strip().lower()
            if choice in ["play again", "quit"]:
                return choice
            else:
                print("Invalid choice. Please type 'Play again' or 'Quit'")

    def play_game(self, game_type):
        if game_type == 'five_card_draw':
            self.deck = Deck(num_decks=6)  # Reset the deck for a new game
            self.ai_difficulty = self.select_ai_difficulty()
            self.players = [Player("Human", is_human=True)]
            self.players += [Player(f"AI_{i}", ai_difficulty=self.ai_difficulty) for i in range(1, 3)]
            self.cheat_manager = CheatManager(self)
            game = FiveCardDrawGame(self.players, self.deck, self.ai_difficulty, self.cheat_manager)
            game.play_round()
        
        
        choice = self.end_game_options()
        if choice == "play again":
            self.play_game(game_type)  # Recursively call to play the same game again
        elif choice == "quit":
            print("Thank you for playing!")
