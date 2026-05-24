from unittest.mock import mock_open, patch

import pandas as pd
import pytest
from mypy.types import Any

from src.read_tansactions import read_csv, read_xls


@pytest.fixture
def transactions_fixture() -> list[dict]:
    result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "366176",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": "29482",
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
    ]
    return result


@pytest.fixture
def csv_stream_fixture() -> str:
    stream = "".join(
        (
            "id;state;date;amount;currency_name;currency_code;from;to;description\n",
            "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;",
            "Счет 39745660563456619397;Перевод организации\n",
            "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;",
            "Discover 0720428384694643;Перевод с карты на карту\n",
            "593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;",
            "Visa 6804119550473710;Перевод с карты на карту\n",
            "366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;",
            "Visa 3820488829287420;Перевод с карты на карту\n",
            "5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада",
        )
    )
    return stream


@patch(
    "builtins.open",
    mock_open(
        read_data="".join(
            (
                "id;state;date;amount;currency_name;currency_code;from;to;description\n",
                "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;",
                "Счет 39745660563456619397;Перевод организации\n",
                "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;",
                "Discover 0720428384694643;Перевод с карты на карту\n",
                "593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;",
                "Visa 6804119550473710;Перевод с карты на карту\n",
                "366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;",
                "Visa 3820488829287420;Перевод с карты на карту\n",
                "5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада",
            )
        )
    ),
)
def test_read_csv_mock1(transactions_fixture: list[dict]) -> None:
    """Тестирование модуля read_csv() с использованием объекта Mock в декораторе patch. Таким образом, мокирукется
    реальное чтение из файла с последующей нормальной работой объекта csv.DictReader"""

    path_csv_file = "transactions.csv"
    assert read_csv(path_csv_file) == transactions_fixture


def test_read_csv_mock2(transactions_fixture: list[dict], csv_stream_fixture: str) -> None:
    """Тестирование модуля read_csv() с использованием объекта Mock в качестве контекстного менеджера. Таким образом,
    мокирукется реальное чтение из файла с последующей нормальной работой объекта csv.DictReader"""

    with patch("builtins.open", mock_open(read_data=csv_stream_fixture)):
        path_csv_file = "transactions.csv"
        assert read_csv(path_csv_file) == transactions_fixture


@patch("pandas.read_excel")
def test_read_exel_mock(mock_read_excel: Any, transactions_fixture: list[dict]) -> None:
    """Тестирование модуля read_xls() с использованием объекта Mock в качестве контекстного менеджера. Таким образом,
    мокирукется реальное чтение из файла"""

    mock_read_excel.return_value = pd.DataFrame(transactions_fixture)
    xls_file_name = "transactions3.xlsx"

    with patch("builtins.open", mock_open(read_data=str(pd.DataFrame(transactions_fixture)))):
        path_xls_file = xls_file_name
        result = read_xls(path_xls_file)
        assert result == transactions_fixture
    mock_read_excel.assert_called()
