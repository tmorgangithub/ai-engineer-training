# Mad Libs — a silly story generator

**Level:** Beginner · you can do this one entirely on your own
**Time:** one short sitting (the easiest of the three — a good confidence builder)

## What you're building

The program asks the player for a bunch of words — a noun, a verb, an adjective, a name, a number — without telling them the story. Then it drops those words into a pre-written story template and prints the result, which is almost always ridiculous. That's the whole joy of it.

This one is light on logic and all about working with **text**. It's the least intimidating project here, which makes it a nice way to rack up a quick win.

## What you'll practice

- `input()` to collect words from the player
- **f-strings** (or another way of inserting variables into text) — this is the star of the show
- storing values in well-named variables
- `print()` for the final story
- (stretch) `random` and a list, if you add multiple stories to pick from

No loops or branching are strictly required for the basic version — this is deliberately gentle.

## Definition of done

1. The program asks the player for several different words (aim for at least five, of different types).
2. It stores each answer in a clearly named variable.
3. It builds a story by inserting those words into a template.
4. It prints the finished story so the inserted words read naturally in place.

## Build it in stages

1. **Collect the words.** Ask for each word with `input()` and store them in variables with obvious names (`animal`, `verb`, `adjective`, ...). Print them back to confirm you captured them.
2. **Write the template.** Write out a short story in your own words, leaving blanks where the collected words go.
3. **Fill it in.** Use f-strings to drop the variables into the story, then print it.
4. **Read it out loud.** Fix any spots where the grammar reads awkwardly no matter what word goes in.

## Hints (not answers)

- An f-string lets you drop a variable straight into text: `print(f"The {animal} jumped over the {adjective} fence.")`.
- Ask for a *variety* of word types — the funniest results come from mixing nouns, verbs, adjectives, a name, and a number.
- Triple-quoted strings (`"""..."""`) are handy for a multi-line story.

## Stretch goals (after "done")

- Write two or three different story templates and use `random.choice` to pick one each run — now you're combining text with the `random` skill you already have.
- Wrap it in a "play again?" loop so the player can generate several stories in a row.
- Let the player pick a theme (spooky / sci-fi / sports) and choose a matching story.

## Checkpoint — show your mentor

Run it in front of your dad and generate a story together. Be ready to explain how the words the player typed ended up inside the sentence — in other words, what the f-string is actually doing. Simple project, real concept.
