def calculate_tometage(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.1
    return wrapper