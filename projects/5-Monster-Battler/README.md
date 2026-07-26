# Project 2 — Monster Battler

**Level:** Intermediate · you can do most of this yourself, but a few parts are meant to send you to your mentor
**Time:** several sittings — build it in stages, don't rush

## What you're building

A tiny turn-based battle game. Your **Hero** fights a series of randomly generated **Monsters**, one at a time. Each turn you choose to *attack* or *defend*; damage is randomized; whoever's health hits zero faints. Beat a whole wave of monsters and you win the game. Lose a fight and it's over.

This is the kind of project that *feels* like a real program — lots of small pieces working together — which is exactly why it's a good stretch.

## What you already know that you'll use

- **Classes** — you just learned the basics, and this project leans on them hard (good reinforcement).
- `random` — for monster stats and damage rolls.
- `while` loops — for the turn loop *and* the wave loop (one inside the other).
- `if` / `elif` / `else` — for turn choices and outcomes.
- lists — for the pool of monster names/types.
- `input()` and `print()` — the whole interface.

## New things you'll meet — this is where your mentor comes in

You'll hit these, and you're *expected* to get stuck on them. That's the point. Attempt each one first, then ask.

1. **Inheritance** — `Hero` and `Monster` will both be built *from* a shared `Character` class instead of repeating the same code twice. The syntax `class Hero(Character):` and the line `super().__init__(...)` are the parts to ask about.
2. **Objects acting on other objects** — when the hero attacks, your code calls a method *on the monster* to reduce its health (`monster.take_damage(...)`). Wrapping your head around "one object changing another object" is a real step up.
3. **Nested loops** — a battle loop (turns) running *inside* a wave loop (monsters). Keeping track of which loop you're in trips everyone up at first.
4. **Return vs. print** — when should a method *return a value* to the caller versus *print* something itself? Worth a conversation.

## Definition of done

1. There's a `Character` class with health, an attack value, a `take_damage(amount)` method, and an `is_alive()` method.
2. `Hero` and `Monster` are both created *using inheritance* from `Character` (not copy-pasted).
3. Monsters are generated with some randomness — random health and/or a random name pulled from a list.
4. A single battle runs as a loop of turns until the hero or the monster faints.
5. On the hero's turn they can choose to **attack** (deal randomized damage) or **defend** (take reduced damage next hit).
6. Beating a monster spawns the next one; clearing a set number of monsters (say 3) wins the game.
7. Clear messages throughout: whose turn, damage dealt, current health, who fainted, victory/defeat.

## Build it in stages

1. **The base.** Write `Character` with health, attack value, `take_damage()`, `is_alive()`. Make one by hand and test the methods in isolation.
2. **Inheritance.** Create `Hero` and `Monster` from `Character`. (This is tutoring point #1 — try, then ask.)
3. **One dumb fight.** Hero and monster take turns auto-attacking until one faints. No choices yet.
4. **Player choice.** Add the attack/defend menu on the hero's turn.
5. **Randomness.** Randomize damage rolls and monster stats.
6. **Waves.** Wrap a single fight in an outer loop so beating one monster brings the next. Add the win condition.
7. **Polish.** Better messages, maybe a healing potion the hero can use once per fight.

## Hints (not answers)

- Give `Character.__init__` parameters like `name`, `health`, and `attack`. Store them as `self.name`, etc.
- `take_damage(amount)` should just subtract from `self.health`. Decide whether to let health go negative or clamp it at zero.
- `random.randint(low, high)` works for both damage rolls and random monster health.
- Pull monster names from a list with `random.choice(["Goblin", "Slime", "Bat"])`.
- For "defend," a simple approach is a flag like `self.defending = True` that halves the next hit, then resets.

## Stretch goals (after "done")

- Add a second monster *type* with its own subclass that overrides how it attacks.
- Give the hero a small inventory (a list or dict) with items.
- Add critical hits (a random chance to double damage).
- (Bigger — heads toward the next project) save the hero's wins to a file so progress persists between runs. Ask your mentor if you want to try this; it introduces file handling.

## Checkpoint — show your mentor

Demo a full run: win at least one fight, then lose one. Then, with the code open, explain two things in your own words — how `take_damage` changes the monster's health, and what `super().__init__` is doing in your subclasses. If you can explain those, you've genuinely learned the hard parts, not just copied them.
