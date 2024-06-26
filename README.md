1. Introduction:
The Task Manager application is designed to provide users with a convenient way to
manage tasks effectively. This document outlines the requirements, functionalities, and
specifications for the development of the Task Manager application.
2. Functional Requirements:
The Task Manager application should fulfill the following functional requirements:
● Users should be able to add tasks by providing a title, description, priority
(High/Medium/Low), and status (Pending/In Progress/Completed).
● Users should be able to edit existing tasks by specifying the task ID and providing
updated information for the title, description, priority, and status.
● Users should be able to delete tasks by specifying the task ID.
● Users should be able to view all tasks to see a list of all existing tasks along with
their details.
● Users should be able to filter tasks by priority to view tasks with a specific priority
level.
3. Class Structure:
The Task Manager application should consist of the following classes:
● Task Class:
● Attributes: id, title, description, priority, status.
● Methods: __init__(), __str__().
● TaskManager Class:
● Attributes: tasks (list of Task objects).
● Methods: __init__(), add_task(), edit_task(), delete_task(),
get_task_by_id(), view_all_tasks(), filter_tasks_by_priority().

4. User Interaction:
● The Task Manager application should provide a command-line interface for user
interaction.
● Users should be presented with a menu containing options to perform various
tasks (add, edit, delete, view all tasks, filter tasks by priority, exit).
● Users should input their choice by entering a corresponding number.
5. Error Handling:
● The Task Manager application should provide error handling for invalid user
inputs, such as incorrect task IDs or priority/status values.
● Error messages should be displayed to guide users in correcting input errors.
