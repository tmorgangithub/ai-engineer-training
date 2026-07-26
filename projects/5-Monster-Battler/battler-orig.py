"""
Monster Battler — starter scaffold.

This scaffold shows you the *shape* of the classes but leaves the real work to
you. Parts marked "ASK YOUR MENTOR" are the ones you're expected to get stuck
on — try them first, then ask.

Run it often as you build:

    python battler.py

You're free to restructure this. It's a starting point, not a cage.
"""

import random


MONSTER_NAMES = ["Goblin", "Slime", "Bat", "Skeleton", "Imp"]
MONSTERS_TO_WIN = 3


class Character:
    """The shared base for anything that can fight: a hero or a monster."""

    def __init__(self, name, health, attack):
        # TODO: store name, health, and attack on self (self.name = name, etc.)
        pass

    def take_damage(self, amount):
        """Reduce this character's health by `amount`."""
        # TODO: subtract from self.health. Decide: clamp at 0, or allow negative?
        pass

    def is_alive(self):
        """Return True if this character still has health left."""
        # TODO: return True/False based on self.health
        pass


class Hero(Character):
    """The player's character. Built FROM Character using inheritance."""

    def __init__(self, name):
        # ASK YOUR MENTOR (#1): how does super().__init__(...) work here, and
        # what values should the hero start with?
        #
        # super().__init__(name, health=?, attack=?)
        self.defending = False  # used by the "defend" action later

    # Later you'll add methods for the hero's turn (attack / defend / heal).


class Monster(Character):
    """An enemy. Also built FROM Character using inheritance."""

    def __init__(self):
        # ASK YOUR MENTOR (#1): generate a random name and random stats,
        # then pass them up to the base class with super().__init__(...).
        pass


def spawn_monster():
    """Create and return a fresh random Monster."""
    # TODO: return Monster()
    pass


def battle(hero, monster):
    """Run one full fight. Return True if the hero survives, False if not."""

    # TODO (the heart of the project):
    #   Loop turns while BOTH hero and monster are alive:
    #     1. Hero's turn: ask attack or defend, then act.
    #        - attacking calls monster.take_damage(<random amount>)
    #     2. If the monster fainted, break and return True.
    #     3. Monster's turn: it attacks the hero (random amount).
    #        - remember to account for the hero defending
    #     4. If the hero fainted, break and return False.
    #   Print health after each exchange so the player can follow along.
    #
    # ASK YOUR MENTOR (#2): notice how the hero's turn changes the MONSTER
    # object, and the monster's turn changes the HERO object.

    return False


def main():
    print("=== Monster Battler ===")
    name = input("Name your hero: ")
    hero = Hero(name)

    defeated = 0

    # ASK YOUR MENTOR (#3): this is the OUTER loop (the wave). Inside it you
    # call battle(), which has its own INNER loop (the turns). Keeping the two
    # straight is the tricky part.
    #
    # TODO: keep spawning monsters and calling battle() until the hero either
    #   dies or defeats MONSTERS_TO_WIN monsters. Print victory or defeat.

    print("Game over.")


if __name__ == "__main__":
    main()
