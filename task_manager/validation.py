from datetime import datetime

def validate_task_title(title):
    if not title or not title.strip():
        return False, "Title cannot be empty."
    return True, title.strip()
    
def validate_task_description(description):
    if not description or not description.strip():
        return False, "Description cannot be empty."
    return True, description.strip()
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD."