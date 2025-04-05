import datetime

tasks = []


def add_task():
    while True:
        try:
            priority = int(input("Enter task priority (1-10): "))
            if 1 <= priority <= 10:
                break
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    tasks.append((priority, due_date))
    print(f"Task added: Priority {priority}, Due Date {due_date}")


def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Priority: {task[0]}, Due Date: {task[1]}")


def bubble_sort_tasks():
    n = len(tasks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tasks[j][0] < tasks[j + 1][0]:
                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
    print("Tasks sorted by priority (highest to lowest) using Bubble Sort.")
    display_tasks()


def find_highest_priority_task():
    if not tasks:
        print("No tasks found.")
    else:
        highest_priority = max(tasks, key=lambda x: x[0])
        print(f"Highest priority task: Priority {highest_priority[0]}, Due Date {highest_priority[1]}")


def remove_task():
    display_tasks()
    while True:
        try:
            task_priority = int(input("Enter the priority of the task to remove: "))
            global tasks
            tasks = [task for task in tasks if task[0] != task_priority]
            print(f"Tasks with priority {task_priority} have been removed.")
            break
        except ValueError:
            print("Please enter a valid number.")


def main_menu():
    while True:
        print("\n--- Task Management System ---")
        print("1. Show task list")
        print("2. Add new task")
        print("3. Remove task by priority")
        print("4. Sort tasks by priority (Bubble Sort)")
        print("5. Find highest priority task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            bubble_sort_tasks()
        elif choice == '5':
            find_highest_priority_task()
        elif choice == '6':
            print("Thank you for using the Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
