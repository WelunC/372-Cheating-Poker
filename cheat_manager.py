# cheat_manager.py

import random
class CheatManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.deck = game_manager.deck  # Access the same deck as the game manager
        self.players = game_manager.players
        self.difficulty = game_manager.ai_difficulty

        # Cheat detection probabilities
        self.cheat_probabilities = {
            "easy": {"swap_card": 0.1, "new_hand": 0.2, "declare_win": 0.5},
            "medium": {"swap_card": 0.2, "new_hand": 0.6, "declare_win": 0.8},
            "hard": {"swap_card": 1, "new_hand": 1, "declare_win": 1},
            "debug": {"swap_card": 0, "new_hand": 0, "declare_win": 0}
        }

        # AI responses
        self.ai_responses = {
            "swap_card": ["Hey, I saw that! No sneaky swaps allowed!", "Nice try, but I’m not falling for that!", "Thought you could slip that by me? Think again!"],
            "new_hand": ["What’s this? An entirely new hand? Caught you!", "Oops! That new hand looks a bit... familiar.", "Did you think I wouldn't notice all new cards? Try again!"],
            "declare_win": ["You win? Not so fast! I'm not that new!", "I don’t remember agreeing to that...", "Nice try, but I’m calling your bullshit!"]
        }

    def shorthand_to_card(self, shorthand):
        #Converts a shorthand card notation (e.g., '9D') into a Card object.
        return self.deck.create_card(shorthand)  # Use the new create_card method in Deck

    def cheat_detection_check(self, cheat_type):
        detection_chance = self.cheat_probabilities[self.difficulty][cheat_type]
        if random.random() < detection_chance:
            print(random.choice(self.ai_responses[cheat_type]))
            return True
        return False

    def attempt_single_card_swap(self):
        card_input = input("Enter the card you want in shorthand (e.g., '8H' for 8 of Hearts, 'KD' for King of Diamonds): ")
        new_card = self.shorthand_to_card(card_input)
        
        if new_card:
            print(f"You have selected {new_card} to add to your hand.")

            # Ask which card to replace
            swap_index = int(input("Enter the position (1-5) of the card you want to replace (1-5): ")) - 1
            if 0 <= swap_index < len(self.players[0].hand):  # Check if the index is valid
                print(f"Replacing {self.players[0].hand[swap_index]} with {new_card}.")
                self.players[0].hand[swap_index] = new_card
                print("You swapped one card in your hand.")
                print(f"Your new hand: {', '.join(str(card) for card in self.players[0].hand)}")

                if self.cheat_detection_check("swap_card"):
                    print("AI detected your attempt to cheat! You are disqualified from this round.")
                    return False  # Cheat detected, return False
                else:
                    print("Cheat successful!")
                    return True  # Cheat was successful and not detected
            else:
                print("Invalid card position. Swap failed.")
        else:
            print("Invalid card choice. Cheat failed.")
        return False  # Cheat failed, return False

    def attempt_entire_hand_swap(self):
        new_hand_input = input("Enter your new hand in shorthand (comma-separated, e.g., 'AH, KD, 10C, QS, 3D'): ")
        new_hand = [self.shorthand_to_card(card_str.strip()) for card_str in new_hand_input.split(',')]
        
        if len(new_hand) == 5 and all(new_hand):
            self.players[0].hand = new_hand
            print("You replaced your entire hand.")

            if self.cheat_detection_check("new_hand"):
                print("AI detected your attempt to cheat! You are disqualified from this round.")
                return False  # Cheat detected, return False
            else:
                print("Cheat successful!")
                return True  # Cheat was successful and not detected
        else:
            print("Invalid hand input. Cheat failed.")
        return False  # Cheat failed, return False

    def attempt_declare_win(self):
        print("Attempting to declare yourself the winner...")
        if self.cheat_detection_check("declare_win"):
            print("AI detected your attempt to cheat! You are disqualified from this round.")
        else:
            print("Congratulations! You declared yourself the \"winner\"...")
