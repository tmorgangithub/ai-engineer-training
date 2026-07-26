"""
Mad Libs — a silly story generator. Starter scaffold.

Fill in the parts marked TODO. This is the gentlest project — mostly about
collecting words and dropping them into text. Run it as you go:

    python madlibs.py

You're free to restructure this however you like.
"""


def main():
    print("=== MAD LIBS ===")
    print("Give me some words and I'll build a story. Don't peek at the ending!\n")

    # TODO 1: collect several words from the player with input().
    #   Use clear variable names. Aim for a mix of word types, for example:
    #   an adjective, a noun, a verb, a name, a number, a place.
    #
    # adjective = input("Give me an adjective: ")
    # animal = input("Give me an animal: ")
    # ...

    # TODO 2: write your story as a template and insert the words with f-strings.
    #   A triple-quoted string is handy for a multi-line story:
    #
    # story = f"""
    # One day, a very {adjective} {animal} decided to {verb} all the way to
    # {place}. Everyone named {name} was amazed...
    # """

    # TODO 3: print the finished story.
    print("\n(your story prints here once you've filled in the TODOs)")


if __name__ == "__main__":
    main()
