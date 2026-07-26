# To-Do List — a menu-driven app

**Level:** Beginner · you can do this one entirely on your own
**Time:** one or two focused sittings

## What you're building

A little command-line to-do list. When it starts, it shows a menu: add a task, view all tasks, remove a task, or quit. The program keeps looping back to that menu until you choose to quit. Your tasks live in a list while the program runs.

This is the most "app-like" of the beginner projects — it has the shape of a real tool — and it's the best bridge to your next project, because managing a *collection of things* is one small step from managing a collection of objects.

## What you'll practice

- lists — adding to them, showing them, removing from them
- a **menu loop**: the classic "show options → read a choice → do the thing → repeat" pattern that shows up in tons of real programs
- `if` / `elif` / `else` to route the user's choice
- `input()` and `print()` for the whole interface
- (optional) a basic class to hold the whole thing together, as a stretch

No `random` this time — this one is about structure, not chance.

## Definition of done

1. On startup, and after every action, the program shows a numbered menu.
2. **Add** lets the user type a task, which gets stored.
3. **View** prints all current tasks in a numbered list (and says something friendly if the list is empty).
4. **Remove** lets the user pick a task by its number and deletes it.
5. **Quit** exits the loop cleanly.
6. Choosing an option that isn't on the menu shows a "not a valid choice" message instead of crashing.
7. The menu keeps coming back until the user quits.

## Build it in stages

1. **The loop and menu.** Print the menu, read a choice, and just print which option they picked. Get the "keep showing the menu until quit" loop working first — before any real features.
2. **Add + view.** Store new tasks in a list. Make "view" print them numbered.
3. **Remove.** Let the user choose a number to delete. Think about what happens if they pick a number that doesn't exist.
4. **Polish.** Handle empty-list cases and invalid menu choices with friendly messages.

## Hints (not answers)

- Start with an empty list: `tasks = []`. `.append()` adds; you can remove by index.
- The menu loop is a `while True:` that only `break`s when the user chooses quit.
- To show tasks *numbered*, you'll want to loop over the list while keeping a count. There's a neat built-in called `enumerate()` that does this — worth looking up, but a manual counter works fine too.
- Users count from 1, but lists start at 0. That off-by-one is the classic bug here — expect it.

## Stretch goals (after "done")

- Add a "mark as done" option (a task could become a small structure holding its text and a done/not-done flag).
- Show a count of how many tasks are left.
- Wrap everything in a `TodoList` class with methods like `add`, `remove`, and `show` — a natural way to reuse the basic classes you've learned, and a real head start on the next project.
- (Later concept — ask first) save tasks to a file so they survive after you close the program. That introduces file handling, which is a Project-3 topic.

## Checkpoint — show your mentor

Run it in front of your dad: add a few tasks, view them, remove one by number, try an invalid choice, then quit. Be ready to explain how your menu loop knows when to stop, and why the number the user types isn't the same as the list index.
