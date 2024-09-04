#Working on Task 4: Rock-Paper-Scissors Game for my CodSoft Python programming internship.
#Developing a fun and interactive game to showcase my Python programming skills.
#Stay tuned for updates!
# -@codsoftintern Sara Dhimdi

import json
from datetime import datetime

class Task:
    def __init__(self, description, priority=None, due_date=None):
        self.id = id(self)
        self.description = description
        self.status = "incomplete"
        self.priority = priority
        self.due_date = due_date

    def mark_completed(self):
        self.status = "completed"

    def mark_incomplete(self):
        self.status = "incomplete"

    def update_description(self, new_description):
        self.description = new_description

    def update_priority(self, new_priority):
        self.priority = new_priority

    def update_due_date(self, new_due_date):
        try:
            self.due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid due date format. Please use YYYY-MM-DD.")

    def __str__(self):
        status_str = "Completed" if self.status == "completed" else "Incomplete"
        due_date_str = f"Due: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ""
        return f"{self.id}. {self.description} ({status_str}, Priority: {self.priority}, {due_date_str})"

def add_task(description, priority=None, due_date=None):
    new_task = Task(description, priority, due_date)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_id):
    try:
        del tasks[task_id - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")
    except IndexError:
        print("Invalid task ID.")

def mark_task_completed(task_id):
    try:
        tasks[task_id - 1].mark_completed()
        save_tasks(tasks)
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task ID.")

def mark_task_incomplete(task_id):
    try:
        tasks[task_id - 1].mark_incomplete()
        save_tasks(tasks)
        print("Task marked as incomplete.")
    except IndexError:
        print("Invalid task ID.")

def update_task_description(task_id, new_description):
    try:
        tasks[task_id - 1].update_description(new_description)
        save_tasks(tasks)
        print("Task description updated.")
    except IndexError:
        print("Invalid task ID.")

def update_task_priority(task_id, new_priority):
    try:
        tasks[task_id - 1].update_priority(new_priority)
        save_tasks(tasks)
        print("Task priority updated.")
    except IndexError:
        print("Invalid task ID.")

def update_task_due_date(task_id, new_due_date):
    try:
        tasks[task_id - 1].update_due_date(new_due_date)
        save_tasks(tasks)
        print("Task due date updated.")
    except IndexError:
        print("Invalid task ID.")

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            task_data = json.load(f)
            return [Task(**task_data) for task_data in task_data]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\nTO-DO List:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Mark task as incomplete")
        print("6. Update task description")
        print("7. Update task priority")
        print("8. Update task due date")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as incomplete: "))
            mark_task_incomplete(task_id)
        elif choice == "6":
            task_id = int(input("Enter task ID to update description: "))
            new_description = input("Enter new description: ")
            update_task_description(task_id, new_description)
        elif choice == "7":
            task_id = int(input("Enter task ID to update priority: "))
            new_priority = input("Enter new priority (high, medium, low): ")
            update_task_priority(task_id, new_priority)
        elif choice == "8":
            task_id = int(input("Enter task ID to update due date: "))
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            update_task_due_date(task_id, new_due_date)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")