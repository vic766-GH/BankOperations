
from functools import wraps

def shorten_words(max_len, *, end_symbol='.'):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return " ".join(f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word for word in result.split())
        return inner
    return wrapper
# Пример использования:

@shorten_words(4, end_symbol='!')
def some_func():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

print(some_func())
