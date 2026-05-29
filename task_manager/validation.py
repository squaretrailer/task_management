from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        return False, "Title cannot be empty."
    return True, title.strip()
    
def validate_task_description(description):
    if len(description.strip()) == 0:
        return False, "Description cannot be empty."
    if len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    return True, description.strip()
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")