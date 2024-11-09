Five Card Draw Poker Game

This is a basic Five Card Draw Poker game where you can play against AI opponents with different difficulty levels. You can also attempt cheats (like swapping cards or declaring a win), but there’s a risk of getting caught



How to Run

Clone this repository and navigate to the project folder:

Run the game by executing main.py:

    python main.py

    Follow the on-screen prompts to play!

Requirements

    Python 3.x (Download from python.org if not installed)


Test cases are in there as well to test each possible poker hand that may come up, this can also be done by hand with the swap hands cheat on debug mode


Developer Guide
Code Structure

    main.py: The entry point of the application. Initializes and runs the game using the GameManager class.
    GameManager: Manages the game flow, including deck setup, AI difficulty selection, and cheat manager setup.
    FiveCardDrawGame: Contains the main game logic, including player turns, hand evaluations, and AI behavior.
    CheatManager: Manages cheat-related actions and cheat detection based on AI difficulty. Includes functions for swapping a single card, swapping the entire hand, and declaring a win.
    Deck: Manages the deck of cards and provides methods for shuffling and drawing cards.
    HandEvaluator: Provides functions to evaluate poker hands, assigning ranks and tie-breaking values.
    Player: Represents each player, storing their hand and providing functions for swapping cards.

Key Functions and Features

    Hand Evaluation: HandEvaluator.evaluate_hand() assesses each player’s hand and returns its rank and value.
    AI Difficulty: The AI adapts its behavior based on difficulty (easy, medium, hard, or debug mode). In debug mode, cheats always succeed, while in harder difficulties, the chance of AI catching cheats increases as well as swapping cards more advantageously.
    Cheat Actions: The CheatManager offers various cheating options:
        attempt_single_card_swap(): Allows the player to replace one card in their hand.
        attempt_entire_hand_swap(): Swaps the player’s entire hand.
        attempt_declare_win(): Attempts to declare an immediate win, with a high detection risk.

Libraries Used

    random: For shuffling cards, AI actions, and determining cheat detection probabilities.
