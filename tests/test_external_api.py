import pytest

from src.external_api import convert_currency

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
    assert convert_currency(date, to_currency, from_currency, amount) == result_converted