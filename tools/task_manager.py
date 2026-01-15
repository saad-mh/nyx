_tasks = []

def add_task(task):
    _tasks.append(task)

def list_tasks():
    return _tasks

def remove_task(index):
    _tasks.pop(index)

def clear_tasks():
    _tasks.clear()