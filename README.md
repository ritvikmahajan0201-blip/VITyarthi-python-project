# To-DO List Creator and List managing methods.
OVERVIEW of project

This is a personal project focused on building a fully functional To-Do List Manager using Python, executed entirely within the console. The core goal is to provide a reliable, interactive tool for tracking and managing tasks, prioritizing a simple and efficient user experience.

Feautures
The program's functionality is divided into an initial task input phase and a main interactive menu loop for manipulation.

The workflow is divided into two distinct phases: setup and ongoing management.

1. Initial Setup
The program starts by initializing the user's task list. It prompts the user for the total number of tasks they need to add immediately. For each task, it collects three pieces of critical input:

The Task Name (which will become the dictionary key).

The Priority Level (an integer input: 1, 2, or 3).

The Initial Status (an integer input: 1 or 2).

2. Management Functions
Two Core Functions handle the heavy lifting for data consistency and display:

priority_lev(priority_level, task, status): This function acts as the data standardization layer. It translates the user's integer input for priority (1, 2, 3) into the corresponding descriptive string ('High', 'Medium', 'Low') before storing or updating the task in dic_tasks.

viewalltasks(): The primary display function. It iterates through the entire dictionary to print a clear, formatted, and numbered list of all tasks, showing the name, current priority, and status for easy viewing.

Technologies/Tools use
1) Visual studio code
2) Github/GitBash
3) Python language
