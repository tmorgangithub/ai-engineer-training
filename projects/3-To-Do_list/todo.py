"""
To-Do List — a menu-driven app. Starter scaffold.

Fill in the parts marked TODO. The comments describe what each piece should do,
but you write the logic. Run it often as you build:

    python todo.py

You're free to restructure this however you like.
"""


def show_menu():
    """Print the menu of choices."""
    print()
    print("=== TO-DO LIST ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")


def add_task(tasks):
    """Ask the user for a task and add it to the list."""
    # TODO: read a task with input() and append it to `tasks`.
    pass


def view_tasks(tasks):
    """Print all tasks, numbered starting at 1."""
    # TODO:
    #   - if the list is empty, print a friendly "nothing here yet" message
    #   - otherwise print each task with a number in front of it
    pass


def remove_task(tasks):
    """Let the user remove a task by its number."""
    # TODO:
    #   - show the numbered tasks (you can reuse view_tasks)
    #   - ask which number to remove, convert it to an int
    #   - remember: the number the user sees (1, 2, 3...) is one MORE than the
    #     list index (0, 1, 2...). Handle a number that doesn't exist without
    #     crashing.
    pass


def main():
    tasks = []  # your tasks live here while the program runs

    # TODO: the menu loop.
    #   Loop forever:
    #     - show the menu
    #     - read the user's choice
    #     - route it: 1 -> add, 2 -> view, 3 -> remove, 4 -> quit (break)
    #     - anything else -> "not a valid choice"
    while True:
        show_menu()
        choice = input("Choose an option: ")
        # TODO: replace this placeholder with the routing logic above.
        break

    print("Goodbye!")


if __name__ == "__main__":
    main()
