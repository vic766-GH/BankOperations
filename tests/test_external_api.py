import json
from unittest.mock import Mock, patch

import pytest
from mypy.fastparse import Any

from src.external_api import convert_currency

# Тестирование конвертации валют с реальным обращением к API


@pytest.mark.parametrize(
    "operation_date, to_currency, from_currency, amount, result_converted",
    [
        ("2019-08-26", "RUB", "RUB", "31957.58", 31957.58),  # Корректные данные
        ("2019-08-26", "RUB", "USD", "8221.378", 543664.91),  # Корректные данные
        (
            "2019-14-26",
            "RUB",
            "USD",
            "8221.378",
            0,
        ),  # Некорректные данные - неверная дата
        (
            "2019-08-26",
            "RUВ",
            "USD",
            "8221.378",
            0,
        ),  # Некорректные данные - неверная валюта (использован
        # символ русской раскладки)
        (
            "2019-14-26",
            "RUВ",
            "USB",
            "8221.378",
            0,
        ),  # Некорректные данные - несуществующая валюта
    ],
)
def test_convert_currency(
    operation_date: str,
    to_currency: str,
    from_currency: str,
    amount: str,
    result_converted: float,
) -> None:
    assert (
        convert_currency(operation_date, to_currency, from_currency, amount)
        == result_converted
    )


# Тестирование конвертации валют с маскированием обращения к API через Mock
@pytest.mark.parametrize(
    "operation_date, to_currency, from_currency, amount, result_converted",
    [
        ("2019-08-26", "RUB", "RUB", "31957.58", 31957.58),  # Корректные данные
        ("2019-08-26", "RUB", "USD", "8221.378", 543664.91),  # Корректные данные
        (
            "2019-14-26",
            "RUB",
            "USD",
            "8221.378",
            0,
        ),  # Некорректные данные - неверная дата
        (
            "2019-08-26",
            "RUВ",
            "USD",
            "8221.378",
            0,
        ),  # Некорректные данные - неверная валюта (использован
        # символ русской раскладки)
        (
            "2019-14-26",
            "RUВ",
            "USB",
            "8221.378",
            0,
        ),  # Некорректные данные - несуществующая валюта
    ],
)
@patch("requests.request")
def test_convert_currency_mock(
    mock_convert_currency: Any,
    operation_date: str,
    to_currency: str,
    from_currency: str,
    amount: str,
    result_converted: float,
) -> None:

    # Подготовка
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps(
        {
            "date": operation_date,
            "historical": True,
            "info": {"rate": 63.672704, "timestamp": 1575763199},
            "query": {"amount": amount, "from": from_currency, "to": to_currency},
            "result": result_converted,
            "success": True,
        }
    )

    mock_convert_currency.return_value = mock_response
    assert (
        convert_currency(operation_date, to_currency, from_currency, amount)
        == result_converted
    )
    mock_convert_currency.assert_called()
