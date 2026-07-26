# Pig — a push-your-luck dice game

**Level:** Beginner · you can do this one entirely on your own
**Time:** one or two focused sittings

## What you're building

You versus the computer. On your turn you roll a die over and over, adding each roll to a running "turn total." You can stop and **bank** those points into your score at any time — but if you ever roll a **1**, you lose everything you built up that turn and your turn ends. First player to reach 100 wins.

The fun is the decision: bank what you have, or push your luck for more?

## What you'll practice

- `random` for rolling the die
- **two** kinds of loop working together: a loop for the rolls within a turn, and a loop for the whole game running turn after turn
- `if` / `elif` / `else` for the "rolled a 1?" and "who won?" logic
- running totals — a turn total and a game score that you keep updating
- `print()` for a clear play-by-play

Everything here is inside what you already know. The interesting part isn't new syntax — it's managing *state* (two different totals) correctly, which is a real skill.

## Definition of done

1. A die roll produces a random number from 1 to 6.
2. On the player's turn they can keep rolling; each roll (2–6) adds to the turn total.
3. Rolling a 1 wipes the turn total and ends the turn immediately.
4. The player can choose to bank at any point, moving the turn total into their score.
5. The computer takes its own turns automatically using some simple rule.
6. The game keeps alternating turns until someone reaches 100, then announces the winner.
7. The output clearly shows each roll, the turn total, and both scores.

## Build it in stages

1. **One roll.** Roll the die and print it. Run it a few times so you trust your randomness.
2. **A human turn.** Loop: roll, add to turn total, and after each roll ask "roll again or bank?". Handle rolling a 1 (turn total to zero, turn over).
3. **Scoring.** Banking adds the turn total to the player's score. Print the score.
4. **The computer's turn.** Give the computer a simple rule — for example, keep rolling until its turn total reaches 20, then bank (unless it rolls a 1 first).
5. **The game loop.** Alternate player and computer turns until one hits 100. Announce the winner.

## Hints (not answers)

- `random.randint(1, 6)` is your die.
- You need **two** variables that do different jobs: `turn_total` (resets every turn) and `score` (lasts the whole game). Keeping these straight is the whole challenge — name them clearly.
- A `while` loop with `break` handles "keep rolling until I bank or roll a 1."
- The computer's "rule" is just an `if` on its `turn_total` — no cleverness required.

## Stretch goals (after "done")

- Make the target score a setting (first to 50 for a quick game, 100 for a long one).
- Give the computer a smarter or riskier personality and see if it wins more.
- Track how many turns each player took and report it at the end.

## Checkpoint — show your mentor

Play a full game in front of your dad. Be ready to explain, in your own words, the difference between your `turn_total` and your `score`, and *why* rolling a 1 only wipes one of them. That distinction is the real lesson here.
