import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "cons") -> Any:
    """
    декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент filename,
    который определяет, куда будут записываться логи: Если filename задан, логи записываются
    в указанный файл (расположен в текущем рабочем каталоге). Иначе логи выводятся в консоль.
    """

    def inner(func: Callable) -> Any:
        """Выполнение настройки вывода процесса логирования работы функции"""

        if filename == "cons" or "." not in filename:
            out_unit = "cons"
        else:
            out_unit = "file"
            log_path = os.path.join(f"{os.getcwd()}", filename)
            if os.path.exists(log_path):
                open_mode = "a"
            else:
                open_mode = "w"
            # open_mode = "w"
            log_file = open(log_path, open_mode, encoding="utf-8")

        @wraps(func)
        def logging(*args: Any, **kwargs: Any) -> Any:
            """Выполнение логирования работы функции"""

            work_start = f"Начало работы: {datetime.now()}"
            print(work_start)
            if out_unit == "file":
                log_file.write(f"{work_start}\n")
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                if out_unit == "file":
                    print("error")
                    log_file.write(f"{inner(func).__name__} error: {err}. Inputs: {args}\n")
                else:
                    print(f"{inner(func).__name__} error: {err}. Inputs: {args}")
            else:
                if out_unit == "file":
                    log_file.write(f"{inner(func).__name__} ok\n")
                    print(result)
                else:
                    print(f"{inner(func).__name__} ok")
            work_end = f"Завершение работы: {datetime.now()}"
            print(f"{work_end}\n")
            if out_unit == "file":
                log_file.write(f"{work_end}\n\n")

        return logging

    return inner


# @log()
# #@log("..\\mylog2.txt")
# def my_function(x: Any, y: Any) -> Any:
#     return x + y
#
#
# my_function(1, 2)
# my_function(1, "2")
# my_function(71, 28)
# my_function(1.25, 3.75)
