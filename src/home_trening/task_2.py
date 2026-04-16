from functools import wraps
import time

def retry(*, retries=3, delay=3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(delay)
            raise Exception('Function call failed after multiple retries.')
        return inner
    return wrapper

