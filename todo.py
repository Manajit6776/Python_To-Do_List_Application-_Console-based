def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def view_tasks(tasks):
    print("\nCurrent Tasks:")
    if not tasks:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Enter new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print("Task added!")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()