import pytest

from src.external_api import convert_currency
from unittest.mock import Mock
from unittest.mock import patch

@pytest.mark.parametrize(
    "date, to_currency, from_currency, amount, result_converted",
    [
        ("2019-08-26", "RUB", "RUB","31957.58",31957.58),  # Корректные данные
        ("2019-08-26", "RUB", "USD","8221.378",543664.91),  # Корректные данные
        ("2019-14-26", "RUB", "USD","8221.378",0),  # Некорректные данные - неверная дата
        ("2019-08-26", "RUВ", "USD","8221.378",0),  # Некорректные данные - неверная валюта (использован
        # символ русской раскладки)
        ("2019-14-26", "RUВ", "USB", "8221.378", 0),  # Некорректные данные - несуществующая валюта
    ]
)

def test_convert_currency(date: str, to_currency: str, from_currency: str, amount: str, result_converted: float) -> \
        None :
    mock_convert_currency = Mock(return_value = 121.15)
    convert_currency = mock_convert_currency
    assert convert_currency(date, to_currency, from_currency, amount) == 121.15
    mock_convert_currency.assert_called()
    mock_convert_currency.assert_called_with(date, to_currency, from_currency, amount)


# @pytest.mark.parametrize(
#     "date, to_currency, from_currency, amount, result_converted",
#     [
#         ("2019-08-26", "RUB", "RUB","31957.58",31957.58),  # Корректные данные
#         ("2019-08-26", "RUB", "USD","8221.378",543664.91),  # Корректные данные
#         ("2019-14-26", "RUB", "USD","8221.378",0),  # Некорректные данные - неверная дата
#         ("2019-08-26", "RUВ", "USD","8221.378",0),  # Некорректные данные - неверная валюта (использован
#         # символ русской раскладки)
#         ("2019-14-26", "RUВ", "USB", "8221.378", 0),  # Некорректные данные - несуществующая валюта
#     ]
# )
@patch('requests.get')
def test_convert_currency(mock_convert_currency) -> None :
    mock_convert_currency.return_value = {
        "date": "2019-12-07",
         "historical": True,
         "info": {
             "rate": 63.672704,
             "timestamp": 1575763199
                },
         "query": {
             "amount": 48150.39,
             "from": "USD",
             "to": "RUB"
                },
         "result": 3065865.529955,
         "success": True
         }

    assert convert_currency("2019-12-07", "USD", "RUB","48150.39") == 3065865.53
    mock_convert_currency.assert_called()
