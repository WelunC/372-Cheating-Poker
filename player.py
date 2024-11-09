# player.py

class Player:
    def __init__(self, name, is_human=False, ai_difficulty="medium"):
        self.name = name
        self.is_human = is_human
        self.hand = []
        self.difficulty = ai_difficulty  # Set the AI difficulty level

    def draw_hand(self, deck):
        # Draw 5 cards for a new hand
        self.hand = [deck.draw_card() for _ in range(5)]

    def show_hand(self):
        # Return a string representation of the player's hand
        return ", ".join(str(card) for card in self.hand)

    def swap_cards(self, indices, deck):
        # Swap specified cards with new cards from the deck
        for index in indices:
            self.hand[index] = deck.draw_card()
