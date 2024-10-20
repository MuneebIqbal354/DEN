<h1 align="center">Task No. 6: To-Do List Application in Python </h1>

This is a simple command-line based To-Do List application implemented in Python. The application allows users to manage tasks by adding, editing, removing, and filtering them. It also supports searching tasks by keywords, sorting tasks by ID or status, and clearing all tasks with confirmation.

## Features

  - **Add Task:** Add a task with a unique ID and description.
  - **View Tasks:** View all tasks with their IDs, descriptions, and statuses (Pending or Completed).
  - **Remove Task:** Remove a task by its unique ID.
  - **Mark as Completed:** Mark a task as completed.
  - **Edit Task:** Edit the description of an existing task.
  - **Search Task:** Search for tasks based on a keyword in their descriptions.
  - **Filter Tasks:** Filter tasks based on their status (Pending or Completed).
  - **Clear All Tasks:** Remove all tasks from the list, with a confirmation prompt.
  - **Sort Tasks:** Sort tasks by ID or status.


## Code

**Class:** `TaskManager`

This class handles the core functionality of the To-Do List application. It manages all tasks using a dictionary where the task ID serves as the key and the task details (description and status) are stored as values.

**Methods:** 

**1. `__init__`:**

  - Initializes the task manager with an empty dictionary `self.tasks = {}` to store the tasks.

**2. `add_task`:**

  - Prompts the user to enter a unique task ID and a description.
  - The task is stored in the dictionary with the task ID as the key and task details (description and status) as values.

**3. `show_tasks`:**

  - Displays all tasks currently stored in the dictionary with their ID, description, and status (Pending/Completed).

**4. `delete_task`:**

  - Removes a task from the list by its unique ID.

**5. `complete_task`:**

  - Marks a task as completed by changing its status from "Pending" to "Completed".

**6. `update_task`:**

  - Allows the user to edit the description of an existing task by providing the task ID.

**7. `search_task`:**

  - Searches tasks based on a keyword entered by the user. The search is performed on the task description.

**8. `filter_tasks`:**

  - Filters and displays tasks based on their status (Pending or Completed).

**9. `clear_tasks`:**

  - Clears all tasks from the list, but only if the user confirms the action by typing "yes".

**10. `sort_tasks`:**

Allows sorting tasks either by task ID or by status. The tasks are displayed after sorting.

**Menu Function:** `task_manager_menu`

This function provides an interactive menu for the user. It repeatedly prompts the user to select an option to perform different actions on the tasks, such as adding, viewing, deleting, or sorting them.

  - **Options Mapping:** The menu uses a dictionary (`options`) to map user inputs (choices) to the respective functions in the `TaskManager` class.
  - **Input Handling:** Each option corresponds to a method call in the `TaskManager` class.


## Example

```python
Task Manager Menu:
1. Add Task
2. View Tasks
3. Remove Task
4. Mark Task as Completed
5. Edit Task
6. Search Task
7. Filter Tasks
8. Clear All Tasks
9. Sort Tasks
10. Exit
```
