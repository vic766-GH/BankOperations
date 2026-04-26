import pytest

from src.utils import get_operations, transaction_tu_rub


@pytest.mark.parametrize(
    "path_to_file, get_dict",
    [
        ("", []),  # некорректные данные - не указан файл для обработки
        ("operations_empty.json", []),  # Некорректные данные - неверный путь к файлу
        ("data/operations_empty.json", []),  # Некорректные данные - пустой файл
        ("data/operations_empty_list.json", []),  # Корректные данные - пустой список
        ("data/operations_not_json.json", []),  # Некорректные данные - некорректный json-файл
        ("data/operations_cut.json", [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              },
              {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                  "amount": "8221.37",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
              }
        ]),  # Корректные данные
    ],
)

def test_get_operations(path_to_file: str, get_dict: dict) -> None:
    assert get_operations(path_to_file) == get_dict

def test_transaction_tu_rub(transaction: dict) -> float:
    assert get_operations(path_to_file) == get_dict
