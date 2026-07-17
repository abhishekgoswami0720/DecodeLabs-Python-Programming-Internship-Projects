my_tasks = []


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Quit")


def add_task():
    task = input("Enter the new task: ").strip()
    if task == "":
        print("⚠️  You can't add an empty task.")
        return
    my_tasks.append(task)
    print(f"✅ Added: '{task}'")


def view_tasks():
    if not my_tasks:
        print("📭 Your to-do list is empty. Add something!")
        return

    print("\n----- YOUR TASKS -----")
    for index, task in enumerate(my_tasks, start=1):
        print(f"{index}. {task}")


def remove_task():
    view_tasks()
    if not my_tasks:
        return
    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(my_tasks):
            removed = my_tasks.pop(choice - 1)
            print(f"🗑️  Removed: '{removed}'")
        else:
            print("⚠️  That task number doesn't exist.")
    except ValueError:
        print("⚠️  Please enter a valid number.")


def main():
    print("Welcome to your Python To-Do List, Junior Developer! 🚀")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye! Your tasks lived only in memory, so they're gone now.")
            break
        else:
            print("⚠️  Invalid choice, please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()