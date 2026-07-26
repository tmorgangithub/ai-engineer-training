"""
Pig — a push-your-luck dice game. Starter scaffold.

Fill in the parts marked TODO. The comments describe the shape of the game,
but you write the logic. Run it often as you build:

    python pig.py

You're free to restructure this however you like.
"""

import random


TARGET_SCORE = 100
COMPUTER_BANKS_AT = 20  # the computer keeps rolling until its turn total hits this


def roll_die():
    """Return a random die roll from 1 to 6."""
    # TODO: return random.randint(...)
    pass


def player_turn(current_score):
    """
    Play the human's turn.
    Return the number of points to ADD to their score (0 if they busted on a 1).
    """
    turn_total = 0

    # TODO:
    #   Loop:
    #     - roll the die, show it
    #     - if it's a 1: print "busted!", set turn_total to 0, and end the turn
    #     - otherwise add it to turn_total and show the turn_total
    #     - ask the player: roll again or bank?
    #       - if they bank: stop looping and keep the turn_total
    #
    # Return turn_total at the end.

    return turn_total


def computer_turn(current_score):
    """
    Play the computer's turn automatically.
    Return the number of points to add to its score.
    """
    turn_total = 0

    # TODO:
    #   Loop:
    #     - roll the die, show it
    #     - if it's a 1: turn_total becomes 0, turn ends
    #     - otherwise add to turn_total
    #     - if turn_total >= COMPUTER_BANKS_AT: the computer banks and stops
    #
    # Return turn_total.

    return turn_total


def main():
    player_score = 0
    computer_score = 0

    print("=== PIG ===")
    print(f"First to {TARGET_SCORE} wins. Roll a 1 and you lose that turn's points.\n")

    # TODO: the game loop.
    #   Alternate: player_turn, then computer_turn.
    #   After each turn, add the returned points to that player's score and show
    #   both scores. Stop as soon as someone reaches TARGET_SCORE, then announce
    #   the winner.

    print("Game over.")


if __name__ == "__main__":
    main()
