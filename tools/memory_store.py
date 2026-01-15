_memory = {}

def remember(key, value):
    _memory[key] = value

def recall(key):
    return _memory.get(key)

def forget(key):
    _memory.pop(key, None)

def list_memory():
    return _memory

def clear_memory():
    _memory.clear()