import unittest
from card_deck import Card, Deck
from hand_evaluator import HandEvaluator

class TestPokerGame(unittest.TestCase):
    
    def setUp(self):
        """Set up deck and hands for testing."""
        self.deck = Deck(num_decks=1)
        self.hand_evaluator = HandEvaluator()
        
    # Hand Evaluation Tests

    def test_royal_flush(self):
        """Test recognition of a Royal Flush hand."""
        hand = [
            Card("Hearts", "10"),
            Card("Hearts", "J"),
            Card("Hearts", "Q"),
            Card("Hearts", "K"),
            Card("Hearts", "A")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Royal Flush")

    def test_straight_flush(self):
        """Test recognition of a Straight Flush hand."""
        hand = [
            Card("Clubs", "5"),
            Card("Clubs", "6"),
            Card("Clubs", "7"),
            Card("Clubs", "8"),
            Card("Clubs", "9")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Straight Flush")

    def test_four_of_a_kind(self):
        """Test recognition of a Four of a Kind hand."""
        hand = [
            Card("Diamonds", "8"),
            Card("Hearts", "8"),
            Card("Clubs", "8"),
            Card("Spades", "8"),
            Card("Diamonds", "3")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Four of a Kind")

    def test_full_house(self):
        """Test recognition of a Full House hand."""
        hand = [
            Card("Clubs", "Q"),
            Card("Diamonds", "Q"),
            Card("Hearts", "Q"),
            Card("Clubs", "7"),
            Card("Diamonds", "7")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Full House")

    def test_flush(self):
        """Test recognition of a Flush hand."""
        hand = [
            Card("Spades", "2"),
            Card("Spades", "5"),
            Card("Spades", "7"),
            Card("Spades", "9"),
            Card("Spades", "K")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Flush")


    def test_three_of_a_kind(self):
        """Test recognition of a Three of a Kind hand."""
        hand = [
            Card("Clubs", "9"),
            Card("Hearts", "9"),
            Card("Diamonds", "9"),
            Card("Spades", "K"),
            Card("Clubs", "7")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Three of a Kind")

    def test_two_pair(self):
        """Test recognition of a Two Pair hand."""
        hand = [
            Card("Clubs", "5"),
            Card("Diamonds", "5"),
            Card("Hearts", "3"),
            Card("Spades", "3"),
            Card("Clubs", "Q")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "Two Pair")

    def test_one_pair(self):
        """Test recognition of a One Pair hand."""
        hand = [
            Card("Hearts", "4"),
            Card("Diamonds", "4"),
            Card("Clubs", "8"),
            Card("Spades", "J"),
            Card("Hearts", "A")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "One Pair")

    def test_high_card(self):
        """Test recognition of a High Card hand."""
        hand = [
            Card("Hearts", "2"),
            Card("Diamonds", "5"),
            Card("Clubs", "9"),
            Card("Spades", "J"),
            Card("Hearts", "A")
        ]
        result = self.hand_evaluator.evaluate_hand(hand)
        self.assertEqual(result[0], "High Card")
    


# Run tests
if __name__ == "__main__":
    unittest.main()
