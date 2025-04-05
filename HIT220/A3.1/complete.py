import sys

# Requirement 1(i): Use a list to store tasks. Each task should be represented as a tuple (priority, due date),
tasks = []

# Requirement 1(ii): Write a function to add a new task to the list.


def add_task():
    try:
        priority = int(input("Enter priority (integer): "))
        due_date = input("Enter due date (YYYY-MM-DD): ")
        task = (priority, due_date)
        tasks.append(task)
        print(f"Task added: Priority={priority}, Due Date={due_date}")
    except ValueError:
        print("Invalid input. Please enter an integer for priority.")


# Requirement 1(iii): Write a function to display all tasks.
def display_tasks(task_list=None):
    if task_list is None:
        task_list = tasks

    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(f"Priority: {task[0]}, Due Date: {task[1]}")


# Requirement 2(i): Implement a simple sorting algorithm to sort tasks by priority (highest priority first). You may use Bubble Sort for simplicity or select another sorting algorithm of your choice. Provide a brief explanation of how your sorting algorithm works.
def sort_tasks_handler():
    sorted_tasks = sort_tasks()
    print("Tasks sorted by priority.")

    display_tasks(sorted_tasks)


def sort_tasks():
    sorted_tasks = tasks.copy()
    n = len(sorted_tasks)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_tasks[j][0] < sorted_tasks[j + 1][0]:
                sorted_tasks[j], sorted_tasks[j +
                                              1] = sorted_tasks[j + 1], sorted_tasks[j]
    return sorted_tasks


# Requirement 3(i): Write a function to find the task with the highest priority.
def find_highest_priority_task():
    if not tasks:
        print("No tasks available.")
    else:
        sorted_tasks = sort_tasks()
        highest_priority_task = sorted_tasks[0]
        print(
            f"Highest Priority Task: Priority={highest_priority_task[0]}, Due Date={highest_priority_task[1]}")


# Requirement 3(ii): Write a function to remove a task by its priority.
def remove_task_by_priority():
    try:
        priority = int(input("Enter priority of task to remove (integer): "))
        global tasks
        tasks = [task for task in tasks if task[0] != priority]
        print(f"Tasks with priority {priority} have been removed.")
    except ValueError:
        print("Invalid input. Please enter an integer for priority.")


def show_menu():
    while True:
        print("\nTask Management System")
        print("1. Show task list")
        print("2. Add new task")
        print("3. Remove task")
        print("4. Sort tasks by priority")
        print("5. Find highest priority task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task_by_priority()
        elif choice == "4":
            sort_tasks_handler()
        elif choice == "5":
            find_highest_priority_task()
        elif choice == "6":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    show_menu()
