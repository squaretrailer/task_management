from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    valid, title = validate_task_title(title)
    if not valid:
        print(title)
        return
    
    valid, description = validate_task_description(description)
    if not valid:
        print(description)
        return
    
    valid, due_date = validate_due_date(due_date)
    if not valid:
        print(due_date)
        return
    
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return
    
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    if tasks[index]["completed"]:
        print("Task already marked as complete.")
        return
    
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    
    if len(pending) == 0:
        print("No pending tasks.")
        return
    
    print("\nPending Tasks:")
    for i, task in enumerate(pending):
        original_index = tasks.index(task)
        print(f"{original_index + 1}. Title: {task['title']}, Due: {task['due_date']}")

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available. Progress: 0%")
        return 0
    
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
    
    progress = (completed / len(tasks)) * 100
    print(f"Progress: {progress:.1f}% ({completed}/{len(tasks)} tasks completed)")
    return progress