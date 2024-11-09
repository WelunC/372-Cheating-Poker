from hand_evaluator import HandEvaluator
import random

class FiveCardDrawGame:
    def __init__(self, players, deck, ai_difficulty, cheat_manager):
        self.players = players
        self.deck = deck
        self.ai_difficulty = ai_difficulty
        self.cheat_manager = cheat_manager  # Dependency on CheatManager for cheat-related functions

    def ai_swap_phase(self, ai_player):
        if ai_player.difficulty == "easy":
            indices = random.sample(range(5), 2)
            ai_player.swap_cards(indices, self.deck)
        elif ai_player.difficulty == "medium":
            indices = [i for i, card in enumerate(ai_player.hand) if HandEvaluator.get_card_value(card) <= 10]
            ai_player.swap_cards(indices, self.deck)
        elif ai_player.difficulty == "hard":
            card_values = [HandEvaluator.get_card_value(card) for card in ai_player.hand]
            value_counts = {v: card_values.count(v) for v in card_values}
            indices = [i for i, card in enumerate(ai_player.hand) if value_counts[HandEvaluator.get_card_value(card)] < 2]
            ai_player.swap_cards(indices, self.deck)
        elif ai_player.difficulty == "debug":
            indices = random.sample(range(5), 2)
            ai_player.swap_cards(indices, self.deck)


    def compare_hands(self):
        best_hand = None
        best_players = []

        for player in self.players:
            hand_rank, rank_value, tie_break_values = HandEvaluator.evaluate_hand(player.hand)
            print(f"{player.name}'s hand: {player.show_hand()} - {hand_rank}")

            current_hand = (rank_value, tie_break_values)

            if best_hand is None or current_hand > best_hand:
                best_hand = current_hand
                best_players = [player]
            elif current_hand == best_hand:
                best_players.append(player)

        if len(best_players) > 1:
            print("\nIt's a tie between: " + ", ".join([player.name for player in best_players]) + "!")
            return None
        else:
            print(f"\n{best_players[0].name} wins with a {HandEvaluator.evaluate_hand(best_players[0].hand)[0]}!")
            return best_players[0]

    def play_round(self):
        self.deck.shuffle()
        for player in self.players:
            player.draw_hand(self.deck)

        human_player = self.players[0]
        print(f"\n{human_player.name}, your hand: {human_player.show_hand()}")

        # Use CheatManager for cheat attempts
        cheat_action = input("Would you like to attempt a cheat? (Enter 'swap', 'replace', 'declare' or 'no'): ").strip().lower()
        cheat_detected = False
        
        if cheat_action == 'swap':
            # Perform the cheat attempt
            cheat_detected = not self.cheat_manager.attempt_single_card_swap()  # False means cheat was detected
        elif cheat_action == 'replace':
            # Perform the cheat attempt
            cheat_detected = not self.cheat_manager.attempt_entire_hand_swap()  # False means cheat was detected
        elif cheat_action == 'declare':
            self.cheat_manager.attempt_declare_win()

        if cheat_detected:
            print(f"{human_player.name} is disqualified for cheating!")
            return  # End the round immediately if caught cheating
        else:
            if cheat_action != 'no' and cheat_action != 'declare':
                print(f"Cheat successful! Proceeding with the round...")

        # After the cheat phase, if the player is still in the game, ask if they want to swap cards normally
        if cheat_action == 'no' or cheat_action == 'declare' or not cheat_detected:
            swap_action = input("Would you like to swap cards normally? (Enter 'yes' or 'no'): ").strip().lower()
            if swap_action == 'yes':
                swap_indices = input("Enter the positions (1-5) of the cards you'd like to swap, separated by commas (e.g., '1,3'): ").strip()
                swap_indices = [int(i) - 1 for i in swap_indices.split(',')]  # Convert to 0-indexed
                human_player.swap_cards(swap_indices, self.deck)
                print(f"Your new hand: {human_player.show_hand()}")

        # If the player is disqualified, skip the AI swap phase
        if cheat_detected:
            return  # End the round if the player was disqualified

        # Continue with AI swap phase and hand comparison if human is not disqualified
        for ai_player in self.players[1:]:
            self.ai_swap_phase(ai_player)

        # If the human player was not disqualified, compare hands to determine the winner
        winner = self.compare_hands()