from card_deck import Card

CARD_VALUE_MAP = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

POKER_HAND_RANKS = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

class HandEvaluator:
    @staticmethod
    def get_card_value(card: Card) -> int:
        """
        Converts card value to integer for sorting purposes.
        Looks up the card value in the CARD_VALUE_MAP for all cards (face cards and numeric).
        """
        card_value = card.get_value()  # Use the card's value directly
        mapped_value = CARD_VALUE_MAP.get(card_value, 0)  # Default to 0 if not found
        return mapped_value

    @staticmethod
    def evaluate_hand(hand):
        """
        Evaluates the hand and returns a tuple (hand rank, rank value, tie-breaking values).
        """
        # Convert card values to integers for proper comparison and sorting
        values = [HandEvaluator.get_card_value(card) for card in hand]  # Keep all values, no set
        suits = [card.suit for card in hand]

        is_flush = len(set(suits)) == 1  # Check if all suits are the same
        is_straight = False

       
        possible_straights = [
            {14, 2, 3, 4, 5},  # Ace low straight (5, 4, 3, 2, Ace)
            {2, 3, 4, 5, 6},   # Straight 2 to 6
            {3, 4, 5, 6, 7},   # Straight 3 to 7
            {4, 5, 6, 7, 8},   # Straight 4 to 8
            {5, 6, 7, 8, 9},   # Straight 5 to 9
            {6, 7, 8, 9, 10},  # Straight 6 to 10
            {7, 8, 9, 10, 11}, # Straight 7 to Jack
            {8, 9, 10, 11, 12},# Straight 8 to Queen
            {9, 10, 11, 12, 13},# Straight 9 to King
            {10, 11, 12, 13, 14} # Straight 10 to Ace (high)
        ]

        # Check if the hand contains a valid straight by comparing the values against the hardcoded combinations
        for straight in possible_straights:
            if set(values) == straight:
                is_straight = True
                break

        # Initialize winning hand and best rank
        winning_hand = ("High Card", POKER_HAND_RANKS["High Card"], values)

        # Check if the hand is a Straight Flush (5 consecutive cards of the same suit)
        if is_straight and is_flush:
            # If it's a straight flush, check if it's a Royal Flush
            royal_flush_values = {10, 11, 12, 13, 14}  # Representing 10 (J), 11 (Q), 12 (K), 13 (A), 14 (K)
            if set(values) == royal_flush_values:
                winning_hand = max(winning_hand, ("Royal Flush", POKER_HAND_RANKS["Royal Flush"], values), key=lambda x: x[1])
            else:
                winning_hand = max(winning_hand, ("Straight Flush", POKER_HAND_RANKS["Straight Flush"], values), key=lambda x: x[1])
        
        # If it's only a flush
        elif is_flush:
            winning_hand = max(winning_hand, ("Flush", POKER_HAND_RANKS["Flush"], values), key=lambda x: x[1])

        # After checking for straights and flushes, check other hand types:
        value_counts = {value: values.count(value) for value in values}  # Count the occurrences of each card value
        sorted_value_counts = sorted(value_counts.items(), key=lambda x: (-x[1], -x[0]))  # Sort by count, then by value

        # Four of a Kind
        if sorted_value_counts[0][1] == 4:
            winning_hand = max(winning_hand, ("Four of a Kind", POKER_HAND_RANKS["Four of a Kind"], [sorted_value_counts[0][0]] + [x[0] for x in sorted_value_counts[1:]]), key=lambda x: x[1])
        # Full House
        elif sorted_value_counts[0][1] == 3 and sorted_value_counts[1][1] == 2:
            winning_hand = max(winning_hand, ("Full House", POKER_HAND_RANKS["Full House"], [sorted_value_counts[0][0], sorted_value_counts[1][0]]), key=lambda x: x[1])
        # Three of a Kind
        elif sorted_value_counts[0][1] == 3:
            winning_hand = max(winning_hand, ("Three of a Kind", POKER_HAND_RANKS["Three of a Kind"], [sorted_value_counts[0][0]] + [x[0] for x in sorted_value_counts[1:]]), key=lambda x: x[1])
        # Two Pair
        elif sorted_value_counts[0][1] == 2 and sorted_value_counts[1][1] == 2:
            winning_hand = max(winning_hand, ("Two Pair", POKER_HAND_RANKS["Two Pair"], [sorted_value_counts[0][0], sorted_value_counts[1][0], sorted_value_counts[2][0]]), key=lambda x: x[1])
        # One Pair
        elif sorted_value_counts[0][1] == 2:
            winning_hand = max(winning_hand, ("One Pair", POKER_HAND_RANKS["One Pair"], [sorted_value_counts[0][0]] + [x[0] for x in sorted_value_counts[1:]]), key=lambda x: x[1])

        return winning_hand
