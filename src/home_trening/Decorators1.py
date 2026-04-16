from time import time


def printing(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func} started")
        result = func(*args, **kwargs)
        print(f"Function {func} finished")
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time for work: {time_2 - time_1}")
        return result

    return wrapper


@printing
@timer
def example():
    for i in range(100000000):
        continue


example()
