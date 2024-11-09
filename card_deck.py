import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def get_value(self):
        # Ensure value is treated as a string for face cards
        if isinstance(self.value, str):
            return self.value
        return str(self.value)  # Otherwise, convert numeric values to string


class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.build_deck()

    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        
        # Create multiple decks by repeating the card set `num_decks` times
        deck = [Card(suit, value) for suit in suits for value in values] * self.num_decks
        random.shuffle(deck)
        return deck

    def shuffle(self):
        #Shuffles the deck of cards after it is created
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            self.cards = self.build_deck()  # Rebuild and reshuffle if deck is empty
            random.shuffle(self.cards)
        return self.cards.pop()

    def create_card(self, card_str):
        #Creates a Card object from a string input like '10H', 'KH', etc.
        card_str = card_str.upper().strip()

        # Split the string into rank and suit, correctly handling 2-character ranks
        ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
        suits = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
        
        # Handle two-character ranks (like '10')
        if len(card_str) == 3:
            rank = card_str[:2]  # '10'
            suit = card_str[2]   # 'H', 'D', 'C', 'S'
        else:
            rank = card_str[0]   # 'J', 'K', 'Q', etc.
            suit = card_str[1]   # 'H', 'D', 'C', 'S'

        # Validate rank and suit
        if rank in ranks and suit in suits:
            full_suit = suits[suit]
            return Card(full_suit, rank)
        else:
            print(f"Invalid card string: {card_str}")  # Debugging invalid card input
            return None
