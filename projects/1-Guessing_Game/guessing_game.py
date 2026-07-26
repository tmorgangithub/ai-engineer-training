"""
Number Guessing Game — starter scaffold.

Fill in the parts marked TODO. The comments walk you through the shape of
the program, but you write the actual logic. Run the file often as you go:

    python guessing_game.py

You do NOT need to keep this exact structure. If you'd rather write it your
own way, do it — this is just a launch point so you're not staring at a blank
file.
"""

import random


# --- Settings you can tweak ---
LOW = 1
HIGH = 100
MAX_ATTEMPTS = 7


def play_one_round():
    """Play a single round. Return True if the player won, False if they lost."""

    # TODO 1: pick a secret number between LOW and HIGH using random.
    secret = None  # replace this

    attempts_used = 0

    # TODO 2: loop until the player guesses correctly OR runs out of attempts.
    #   - read a guess with input(), convert it to an int
    #   - add 1 to attempts_used
    #   - compare the guess to `secret` and print "too high" / "too low"
    #   - if correct: print a congrats message (with attempts_used) and win
    #   - if attempts run out: print the secret and lose
    #
    # A `while` loop is the right tool here.

    # TODO 3: return True for a win or False for a loss.
    return False


def main():
    print(f"Guess my number between {LOW} and {HIGH}. You have {MAX_ATTEMPTS} tries.")

    # TODO 4: wrap play_one_round() in a loop that asks "play again? (y/n)"
    #   and keeps playing while the answer is yes.
    play_one_round()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
