from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "unit, num_1, num_2, result",
    [
        ("mylog.txt", 1, 2, 3),  # корректные данные
        ("mylog.txt", 1, "2", "error"),
        ("mylog.txt", 71, 28, 99),
        ("mylog.txt", 1.25, 3.75, 5.0),
        ("cons", 1, 2, 3),
        ("cons", 1, "2", "unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2')"),
        ("cons", 71, 28, 99),
        ("cons", 1.25, 3.75, 5.0),
        ("", 1, 2, 3),
        ("", 1, "2", "unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2')"),
        ("", 71, 28, 99),
        ("", 1.25, 3.75, 5.0),  # некорректные данные - пустая строка
        ("monitor", 1, 2, 3),
        ("monitor", 1, "2", "unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2')"),
        ("monitor", 71, 28, 99),
        ("monitor", 1.25, 3.75, 5.0),
    ],
)
def test_decorator(unit: str, num_1: Any, num_2: Any, result: Any, capsys: Any) -> Any:
    """Тест декоратора с параметрами из модуля decorators.py\n При тестировании из логов исключается дата и время.
    Остаётся только фиксация начала работы функции, результат работы и завершение работы функции"""

    # assert my_function(num_1, num_2) == result
    @log(unit)
    def my_function_summ(x: Any, y: Any) -> Any:
        """Простая функция суммирования двух чисел"""
        return x + y

    my_function_summ(num_1, num_2)
    captured = capsys.readouterr()
    if "." in unit:
        assert captured.out[:14] == "Начало работы:"
        assert captured.out[42 : 42 + len(str(result))] == f"{result}"
        assert captured.out[len(captured.out) - 47 : len(captured.out) - 29] == "Завершение работы:"
    else:
        assert captured.out[:14] == "Начало работы:"
        if type(num_1) in (int, float) and type(num_2) in (int, float):
            assert captured.out[42:61] == "my_function_summ ok"
            assert captured.out[62 : len(captured.out) - 29] == "Завершение работы:"
        else:
            assert captured.out[66:100] == "unsupported operand type(s) for +:"
            assert captured.out[135 : len(captured.out) - 29] == "Завершение работы:"
