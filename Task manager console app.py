class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

task_list = []
next_id = 1

def create_task():
    global next_id
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(next_id, title, description)
    task_list.append(task)
    print("Task added successfully.")
    next_id += 1

def read_tasks():
    if not task_list:
        print("No tasks found.")
    else:
        print("\n--- Task List ---")
        for task in task_list:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")

def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in task_list:
        if task.id == task_id:
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            print(" Task updated successfully.")
            return
    print(" Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            print("🗑️ Task deleted successfully.")
            return
    print(" Task not found.")

def menu():
    while True:
        print("\nTask Manager Menu")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

# Start the application
menu()
