def round_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) is float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) is float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


@round_numbers
def test_func(x, y):
    result = type(x)([x1 / y for x1 in x])
    return result


res = test_func([3, 7, 5, 4, 11, 21], 3)
print(res)
