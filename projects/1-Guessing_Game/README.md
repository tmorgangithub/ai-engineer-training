# Project 1 — Number Guessing Game - Hello



**Level:** Beginner · you can do this one entirely on your own
**Time:** roughly one focused sitting or two

## What you're building

The computer secretly picks a number in a range. You guess. After each guess the program tells you whether the secret is *higher* or *lower*, and you keep guessing until you get it or run out of attempts. When the round ends, it asks if you want to play again.

That's it. Simple on the surface, but you'll touch almost every basic tool you've learned.

## What you'll practice

- `random` for picking the secret number
- `while` loops for repeating guesses and for "play again"
- `if` / `elif` / `else` for the higher/lower/correct logic
- `input()` and converting text to a number with `int()`
- comparison operators (`<`, `>`, `==`)
- `print()` for all the feedback

Nothing here needs classes or anything you haven't seen. Resist the urge to look things up beyond the standard `random` docs — you already have everything you need.

## Definition of done

Your program is finished when all of these are true:

1. It picks a random secret number in a fixed range (say 1–100).
2. It reads a guess from the player and turns it into a number.
3. It tells the player "too high" or "too low" after a wrong guess.
4. It congratulates the player on a correct guess and says how many tries it took.
5. It enforces a maximum number of attempts and shows a "you lost, the number was X" message when they run out.
6. After a round ends (win or lose), it asks whether to play again, and actually starts a fresh round if the answer is yes.

## Build it in stages

Don't try to write the whole thing at once. Get each stage *working and tested* before moving to the next.

1. **Pick + one guess.** Pick the secret, read one guess, print whether it matches. Run it a few times.
2. **Loop the guesses.** Wrap the guess in a `while` loop so the player keeps guessing until correct. Add the higher/lower hints.
3. **Attempt limit.** Count the guesses. Stop and show a loss message when the count hits the limit.
4. **Play again.** Wrap the whole round in an outer loop that asks "play again? (y/n)".
5. **Difficulty (optional).** Let the player pick easy/medium/hard, which changes the range and/or the number of attempts.

## Hints (not answers)

- `random.randint(1, 100)` gives you a whole number from 1 to 100 inclusive.
- A `while True:` loop with a `break` is a clean way to keep going "until something happens."
- `int(input("Your guess: "))` reads text and converts it in one line. (What happens if the player types "banana"? Note it — you'll fix that kind of thing properly in Project 2. For now, assume they type numbers.)
- Keep a counter variable that you add `1` to each time through the guess loop.

## Stretch goals (only after "done")

- Track the *best* (fewest) number of guesses across rounds and show it as a high score.
- Add a difficulty menu that changes range and attempt count.
- Wrap the whole game in a class called `GuessingGame` — a gentle way to reuse the "basic classes" you just learned.

## Checkpoint — show your mentor

Run it in front of your dad and demonstrate: a win, a loss (run out of attempts), and a successful "play again." Be ready to explain, in your own words, why you used a loop where you did.
