import pytest

from src.utils import get_operations, transaction_tu_rub
from unittest.mock import Mock
from unittest.mock import patch

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
    mock_operations = Mock(return_value = [])
    get_operations = mock_operations
    assert get_operations(path_to_file) == []
    mock_operations.assert_called()
    mock_operations.assert_called_with(path_to_file)

@pytest.mark.parametrize(
    "transaction, amount_rub",
    [
        (None, 0),  # некорректные данные - не задан словарь для обработки
        ([], 0),  # некорректные данные - не задан словарь для обработки
        ({}, 0),  # Некорректные данные - пустой словарь для обработки
        ({
             "id": 441945886,
             "state": "EXECUTED",
             "date": "2019-08-26T10:50:58.294041",
             "operationAmount": {
                 "amount": "31957.58",
                 "currency": {
                     "name": "руб.",
                     "code": "RUB"
                 },
                 "description": "Перевод организации",
                 "from": "Maestro 1596837868705199",
                 "to": "Счет 64686473678894779589"
             }
         }, 31957.58),  #Корректные данные
        ({
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
              }, 520543.42)  # Корректные данные
    ]
)

def test_transaction_tu_rub(transaction: dict, amount_rub: float) -> float:
    mock_transaction_tu_rub = Mock(return_value = 121.15)
    get_transaction_tu_rub = mock_transaction_tu_rub
    assert get_transaction_tu_rub(transaction) == 121.15
    mock_transaction_tu_rub.assert_called()
    mock_transaction_tu_rub.assert_called_with(transaction)
