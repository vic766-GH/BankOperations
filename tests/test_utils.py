from unittest.mock import Mock

import pytest

from src.utils import get_operations, transaction_to_rub


@pytest.mark.parametrize(
    "path_to_file, get_dict",
    [
        ("", []),  # некорректные данные - не указан файл для обработки
        ("../operations_empty.json", []),  # Некорректные данные - неверный путь к файлу
        ("operations_empty.json", []),  # Некорректные данные - пустой файл
        ("operations_empty_list.json", []),  # Корректные данные - пустой список
        ("operations_not_json.json", [],),  # Некорректные данные - некорректный json-файл
        (
            "operations_cut.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {
                        "amount": "8221.37",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
            ],
        ),  # Корректные данные
    ],
)
def test_get_operations(path_to_file: str, get_dict: dict) -> None:
    assert get_operations(path_to_file) == get_dict


def test_get_operations_mock() -> None:
    mock_operations = Mock(return_value=[])
    get_operations = mock_operations
    assert get_operations("data/operations_cut.json") == []
    mock_operations.assert_called()
    # mock_operations.assert_called_with("data/operations_cut.json")


@pytest.mark.parametrize(
    "transaction, amount_rub",
    [
        (None, 0),  # некорректные данные - не задан словарь для обработки
        ([], 0),  # некорректные данные - не задан словарь для обработки
        ({}, 0),  # Некорректные данные - пустой словарь для обработки
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
            },
            31957.58,
        ),  # Корректные данные
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            520543.42,
        ),  # Корректные данные
    ],
)
def test_transaction_to_rub(transaction: dict, amount_rub: float) -> None:
    assert transaction_to_rub(transaction) == amount_rub


def test_transaction_tu_rub_mock() -> None:
    mock_transaction_tu_rub = Mock(return_value=121.15)
    get_transaction_tu_rub = mock_transaction_tu_rub
    assert (
        get_transaction_tu_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 121.15
    )
    mock_transaction_tu_rub.assert_called()
    mock_transaction_tu_rub.assert_called_with(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
