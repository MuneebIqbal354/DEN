class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        try:
            task_id = int(input("Enter a unique Task ID: "))
            if task_id in self.tasks:
                print(f"Task ID {task_id} already exists. Please choose a different ID.")
                return
            description = input("Enter task description: ")
            self.tasks[task_id] = {'Description': description, 'Status': 'Pending'}
            print(f"Task {task_id} added successfully.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nCurrent Task List:")
        for task_id, details in self.tasks.items():
            print(f"ID: {task_id}, Description: {details['Description']}, Status: {details['Status']}")
        print()

    def delete_task(self):
        try:
            task_id = int(input("Enter the Task ID to remove: "))
            if task_id in self.tasks:
                del self.tasks[task_id]
                print(f"Task {task_id} deleted.")
            else:
                print(f"Task ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")

    def complete_task(self):
        try:
            task_id = int(input("Enter the Task ID to mark as completed: "))
            if task_id in self.tasks:
                self.tasks[task_id]['Status'] = 'Completed'
                print(f"Task {task_id} is now completed.")
            else:
                print(f"Task ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")

    def update_task(self):
        try:
            task_id = int(input("Enter the Task ID to edit: "))
            if task_id in self.tasks:
                new_desc = input("Enter the new description: ")
                self.tasks[task_id]['Description'] = new_desc
                print(f"Task {task_id} description updated.")
            else:
                print(f"Task ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")

    def search_task(self):
        search_term = input("Enter a keyword to search for: ").lower()
        found_tasks = {tid: details for tid, details in self.tasks.items() if search_term in details['Description'].lower()}
        if found_tasks:
            print("\nMatching tasks:")
            for task_id, details in found_tasks.items():
                print(f"ID: {task_id}, Description: {details['Description']}, Status: {details['Status']}")
        else:
            print(f"No tasks found containing '{search_term}'.")

    def filter_tasks(self):
        filter_status = input("Show tasks with status (Pending/Completed): ").capitalize()
        filtered_tasks = {tid: details for tid, details in self.tasks.items() if details['Status'] == filter_status}
        if filtered_tasks:
            print(f"\nFiltered {filter_status} tasks:")
            for task_id, details in filtered_tasks.items():
                print(f"ID: {task_id}, Description: {details['Description']}")
        else:
            print(f"No {filter_status} tasks found.")

    def clear_tasks(self):
        confirm = input("Are you sure you want to clear all tasks? Type 'yes' to confirm: ").lower()
        if confirm == 'yes':
            self.tasks.clear()
            print("All tasks have been cleared.")
        else:
            print("Action canceled.")

    def sort_tasks(self):
        sort_by = input("Sort tasks by (ID/Status): ").capitalize()
        if sort_by == 'Id':
            sorted_tasks = dict(sorted(self.tasks.items()))
        elif sort_by == 'Status':
            sorted_tasks = dict(sorted(self.tasks.items(), key=lambda item: item[1]['Status']))
        else:
            print("Invalid sort option. Sorting by ID as default.")
            sorted_tasks = dict(sorted(self.tasks.items()))
        
        self.tasks = sorted_tasks
        print(f"Tasks sorted by {sort_by.lower()}.")
        self.show_tasks()

# Menu for Task Manager
def task_manager_menu():
    manager = TaskManager()
    
    options = {
        '1': manager.add_task,
        '2': manager.show_tasks,
        '3': manager.delete_task,
        '4': manager.complete_task,
        '5': manager.update_task,
        '6': manager.search_task,
        '7': manager.filter_tasks,
        '8': manager.clear_tasks,
        '9': manager.sort_tasks,
        '10': lambda: print("Exiting the program.")
    }
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("10. Exit")
        
        user_choice = input("Select an option (1-10): ")
        
        action = options.get(user_choice, None)
        if action:
            action()
            if user_choice == '10':
                break
        else:
            print("Invalid option. Please try again.")

# Run the task manager menu
task_manager_menu()
