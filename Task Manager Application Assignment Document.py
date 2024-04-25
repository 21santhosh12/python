class Task:
    def __init__(self,task_id,title,description,priority,status):
        self.id=task_id
        self.title=title
        self.description=description
        self.priority=priority
        self.status=status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description:{self.description}, Priority:{self.priority}, Status: {self.status}"
    

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append(task)
    def edit_task(self,task_id,title,description,priority,status):
        for task in self.tasks:
            if task.id == task_id:
                task.title=title
                task.descrition = description
                task.priority=priority
                task.status=status
                print("Task was updated")
                break
    
    def delete_task(self,task_id):
        self.tasks=[task for task in self.tasks if task.id!=task_id]
    
    def get_task_by_id(self,task_id):
        for task in self.tasks:
            if task.id==task_id:
                return task
        return None
    
    def view_all_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self,priority):
        filtered_tasks=[task for task in self.tasks if task.priority==priority]
        for task in filtered_tasks:
            print(task)


def display_menu():
    print("Task Manager Menu:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")

def main():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = input("Enter task ID: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, priority, status)
            task_manager.add_task(task)
        elif choice == "2":
            task_id = input("Enter task ID to edit: ")
            title = input("Enter updated title: ")
            description = input("Enter updated description: ")
            priority = input("Enter updated priority: ")
            status = input("Enter updated status: ")
            task_manager.edit_task(task_id, title, description, priority, status)
        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_manager.view_all_tasks()
        elif choice == "5":
            priority = input("Enter priority to filter tasks (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
