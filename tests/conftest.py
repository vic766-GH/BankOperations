import pytest


#
# @pytest.fixture
# def card_number_data() :
#     return [
#     ('7000792289606361', '7000 79** **** 6361'), # корректные данные
#     ("", ""), # некорректные данные - пустая строка
#     ("700079228966361", ""), # некорректные данные - короткая строка - менее 16 символов
#     ('70007922896O6361', ""), # некорректные данные - присутствует не цифра - вместо 0 - O
# ]
#
# @pytest.fixture
# def card_account_data() :
#     return [
#     ('73654108430135874305', '**4305'), # корректные данные
#     ("", ""), # некорректные данные - пустая строка
#     ("736541084301358", ""), # некорректные данные - короткая строка - менее 20 символов
#     ('70007922896O6361', ""), # некорректные данные - присутствует не цифра - вместо 0 - O
# ]
@pytest.fixture
def date_correct() -> str:
    return "2019-07-03T18:35:29.512361"  # корректные данные


@pytest.fixture
def date_month_err() -> str:
    return "2019-14-03T18:35:29.512362"  # некорректные данные - месяц вне допустимого диапазона


@pytest.fixture
def date_day_err() -> str:
    return "2019-07-32T18:35:29.512363"  # некорректные данные - день вне допустимого диапазона


@pytest.fixture
def unsorted_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def executed_select_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def canceled_select_list() -> list:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def one_operation_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_in_descending_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sorted_in_ascending_list() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def empty_list() -> list:
    return []


@pytest.fixture
def unselected_transactions_list() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def usd_select_list() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def rub_select_list() -> list:
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def description_list() -> list:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def card_number_generated_list() -> list:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


@pytest.fixture
def matrix_gen_2_1() -> list:
    return [[[0, 0], [0, 1]], [[0, 0], [2, 1]], [[3, 0], [2, 1]], [[3, 4], [2, 1]]]


@pytest.fixture
def matrix_gen_3_1() -> list:
    return [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 2], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 2], [0, 0, 3]],
        [[0, 0, 0], [0, 1, 2], [0, 4, 3]],
        [[0, 0, 0], [0, 1, 2], [5, 4, 3]],
        [[0, 0, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 0, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 8, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 8, 9], [6, 1, 2], [5, 4, 3]],
    ]


# @pytest.fixture
# def currency_convert_data() -> list:
#     return [
#         ("2019-12-07", "RUB", "USD", "48150.39", 3065865.53),  # Корректные данные
#         ("2019-12-07", "RUB", "USB", "48150.39", 0),  # неверная валюта для конвертации
#         ("2019-12-07", "SUB", "USD", "48150.39", 0),  # неверная валюта в которую конвертируем
#         ("2019-12-07", "SUB", "USB", "48150.39", 0),  # неверная валюта в обоих случаях
#         ("2019-12-07", "SUВ", "USD", "48150.39", 0),  # неверная валюта в которую конвертируем - использован символ в
#         # русской раскладке
#         ("2019-14-07", "RUВ", "USD", "48150.39", 0),  # неверная дата - ошибка в месяце
#         ("2019-14-07", "RUВ", "USD", "4815О.39", 0),  # неверное количество для конвертации - вместо 0 присутствует О
#     ]

@pytest.fixture
def test_transactions_dict_json() -> list[dict]:
    return [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
             'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
             'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
            {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
             'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
            {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368,
             'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
             'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
            {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482,
             'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
             'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
            {'id': 5380041, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789,
             'currency_name': 'Peso', 'currency_code': 'UYU', 'from': None,
             'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
            {'id': 1962667, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588,
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
             'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
            {'id': 5294458, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836,
             'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
             'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
            {'id': 5429839, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261,
             'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': None,
             'to': 'Счет 76768135089446747029', 'description': 'Открытие вклада'},
            {'id': 3226899, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680,
             'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': None,
             'to': 'Счет 88329674734590848775', 'description': 'Открытие вклада'},
            {'id': 3176764, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652,
             'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
             'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'},
            {'id': 4234093, 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z', 'amount': 23182,
             'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Visa 0773092093872450',
             'to': 'Discover 8602781449570491', 'description': 'Перевод с карты на карту'},
            {'id': 3107343, 'state': 'EXECUTED', 'date': '2023-01-25T13:33:00Z', 'amount': 33639,
             'currency_name': 'Krona', 'currency_code': 'SEK', 'from': None,
             'to': 'Счет 35662766798195077538', 'description': 'Открытие вклада'},
            {'id': 2130098, 'state': 'PENDING', 'date': '2020-06-07T11:11:36Z', 'amount': 30731,
             'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Visa 5749750597771353',
             'to': 'American Express 9106381490184499', 'description': 'Перевод с карты на карту'},
            {'id': 4653427, 'state': 'PENDING', 'date': '2020-10-04T12:12:23Z', 'amount': 34072,
             'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Discover 9058011549803523',
             'to': 'Mastercard 5266726031439012', 'description': 'Перевод с карты на карту'},
            {'id': 4641894, 'state': 'EXECUTED', 'date': '2021-08-30T12:27:22Z', 'amount': 11111,
             'currency_name': 'Krona', 'currency_code': 'SEK', 'from': None,
             'to': 'Счет 53688013223998817599', 'description': 'Открытие вклада'}
            ]


@pytest.fixture
def test_transactions_dict_csv() -> list[dict]:
    return [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
         'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368',
         'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
         'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482',
         'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
         'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
        {'id': '5380041', 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': '23789',
         'currency_name': 'Peso', 'currency_code': 'UYU', 'from': '',
         'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
        {'id': '1962667', 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': '18588',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
         'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
        {'id': '5294458', 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': '16836',
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
         'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
        {'id': '5429839', 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': '25261',
         'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': '',
         'to': 'Счет 76768135089446747029', 'description': 'Открытие вклада'},
        {'id': '3226899', 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': '21680',
         'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': '',
         'to': 'Счет 88329674734590848775', 'description': 'Открытие вклада'},
        {'id': '3176764', 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': '16652',
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
         'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'},
        {'id': '4234093', 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z', 'amount': '23182',
         'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Visa 0773092093872450',
         'to': 'Discover 8602781449570491', 'description': 'Перевод с карты на карту'},
        {'id': '3107343', 'state': 'EXECUTED', 'date': '2023-01-25T13:33:00Z', 'amount': '33639',
         'currency_name': 'Krona', 'currency_code': 'SEK', 'from': '',
         'to': 'Счет 35662766798195077538', 'description': 'Открытие вклада'},
        {'id': '2130098', 'state': 'PENDING', 'date': '2020-06-07T11:11:36Z', 'amount': '30731',
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Visa 5749750597771353',
         'to': 'American Express 9106381490184499', 'description': 'Перевод с карты на карту'},
        {'id': '4653427', 'state': 'PENDING', 'date': '2020-10-04T12:12:23Z', 'amount': '34072',
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Discover 9058011549803523',
         'to': 'Mastercard 5266726031439012', 'description': 'Перевод с карты на карту'},
        {'id': '4641894', 'state': 'EXECUTED', 'date': '2021-08-30T12:27:22Z', 'amount': '11111',
         'currency_name': 'Krona', 'currency_code': 'SEK', 'from': '',
         'to': 'Счет 53688013223998817599', 'description': 'Открытие вклада'}
    ]

@pytest.fixture
def test_transactions_dict_xlsx() -> list[dict]:
    return [
        {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
         'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368,
         'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
         'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482,
         'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
         'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
        {'id': 5380041, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789,
         'currency_name': 'Peso', 'currency_code': 'UYU', 'from': '',
         'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
        {'id': 1962667, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588,
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
         'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
        {'id': 5294458, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
         'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
        {'id': 5429839, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261,
         'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': '',
         'to': 'Счет 76768135089446747029', 'description': 'Открытие вклада'},
        {'id': 3226899, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680,
         'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': '',
         'to': 'Счет 88329674734590848775', 'description': 'Открытие вклада'},
        {'id': 3176764, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
         'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'},
        {'id': 4234093, 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z', 'amount': 23182,
         'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Visa 0773092093872450',
         'to': 'Discover 8602781449570491', 'description': 'Перевод с карты на карту'},
        {'id': 3107343, 'state': 'EXECUTED', 'date': '2023-01-25T13:33:00Z', 'amount': 33639,
         'currency_name': 'Krona', 'currency_code': 'SEK', 'from': '',
         'to': 'Счет 35662766798195077538', 'description': 'Открытие вклада'},
        {'id': 2130098, 'state': 'PENDING', 'date': '2020-06-07T11:11:36Z', 'amount': 30731,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Visa 5749750597771353',
         'to': 'American Express 9106381490184499', 'description': 'Перевод с карты на карту'},
        {'id': 4653427, 'state': 'PENDING', 'date': '2020-10-04T12:12:23Z', 'amount': 34072,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Discover 9058011549803523',
         'to': 'Mastercard 5266726031439012', 'description': 'Перевод с карты на карту'},
        {'id': 4641894, 'state': 'EXECUTED', 'date': '2021-08-30T12:27:22Z', 'amount': 11111,
         'currency_name': 'Krona', 'currency_code': 'SEK', 'from': '',
         'to': 'Счет 53688013223998817599', 'description': 'Открытие вклада'}
    ]


# @pytest.fixture
# def test_transactions_dict_outprint() -> list[str]:
#     return [
#         '''Всего банковских операций в выборке: 12\nРаспечатываю итоговый список транзакций...\n\n''',
#         '''05.09.2023 Перевод организации\nСчет **3391 -> Счет **9397\nСумма: 16210 PEN\n\n''',
#         '''06.12.2020 Перевод с карты на карту\nDiscover 3172 60** **** 0065 -> Discover 0720 42** **** 4643\n
#         Сумма: 29740 COP\n\n''',
#         '''02.08.2020 Перевод с карты на карту\nDiscover 0325 95** **** 4937 -> Visa 3820 48** **** 7420\n
#         Сумма: 29482 IDR\n\n''',
#         '''22.10.2023 Перевод организации\nMastercard 7286 84** **** 1431 -> Счет **3144'\nСумма: 18588 COP\n\n''',
#         '''20.06.2022 Перевод с карты на карту\nVisa 2759 01** **** 7198 -> Счет **1082\nСумма: 16836 CNY\n\n''',
#         '''23.06.2023 Открытие вклада\nСчет **7029\nСумма: 25261 UAH\n\n''',
#         '''17.04.2023 Открытие вклада\nСчет **8775\nСумма: 21680 CZK\n\n''',
#         '''08.07.2021 Перевод с карты на карту\nVisa 0773 09** **** 2450 -> Discover 8602 78** **** 0491\n
#         Сумма: 23182 RUB\n\n''',
#         '''25.01.2023 Открытие вклада\nСчет **7538\nСумма: 33639 SEK\n\n''',
#         '''22.07.2023 Перевод с карты на карту\nVisa 1959 23** **** 4097 -> Visa 6804 11** **** 3710\n
#         Сумма: 30368 TZS\n\n''',
#         '''01.02.2021 Открытие вклада\nСчет **5683\nСумма: 23789 UYU\n\n''',
#         '''24.08.2022 Перевод с карты на карту\nMastercard 8387 03** **** 1294 -> American Express 5556 52** ****
#         8852\nСумма: 16652 EUR\n\n'''
#     ]

@pytest.fixture
def test_transactions_dict_empty() -> list[dict]:
    return []