import os
import time
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any
from functools import wraps


def log(filename: str = "cons"):
    """
    декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент filename,
    который определяет, куда будут записываться логи: Если filename задан, логи записываются
    в указанный файл (расположен в текущем рабочем каталоге). Иначе логи выводятся в консоль.
    """

    def inner(func):
        if filename == "cons":
            log_file = filename
        else:
            log_path = os.path.join(f"{os.getcwd()}", filename)
            # if os.path.exists(log_path):
            #     open_mode = "a"
            # else:
            #     open_mode = "w"
            open_mode = "w"
            log_file = open(log_path, open_mode, encoding="utf-8")

        @wraps(func)
        def logging(*args, **kwargs):
            if filename != 'cons':
                print(f"\nНачало работы: {datetime.now()}")
            out_string(log_file, f"Начало работы: {datetime.now()}\n")
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                out_string(log_file, f"{inner(func).__name__} error: {err}. Inputs: {args}\n")
                if filename != 'cons':
                    print('error')
            else:
                out_string(log_file, f"{inner(func).__name__} ok\n")
                if filename != 'cons':
                    print(result)
            out_string(log_file, f"Завершение работы: {datetime.now()}\n\n")
            if filename != "cons":
                print(f"Завершение работы: {datetime.now()}\n")
        return logging
    return inner


def out_string(unit: Any, message: str):
    if unit == "cons":
        print(message)
    else:
        unit.write(message)


#@log()
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
my_function(1, '2')
my_function(71, 28)

