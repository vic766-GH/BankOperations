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
def date_correct():
    return "2019-07-03T18:35:29.512361"  # корректные данные

@pytest.fixture
def date_month_err():
    return "2019-14-03T18:35:29.512362"  # некорректные данные - месяц вне допустимого диапазона

@pytest.fixture
def date_day_err():
    return "2019-07-32T18:35:29.512363"  # некорректные данные - день вне допустимого диапазона

@pytest.fixture
def unsorted_list():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

@pytest.fixture
def executed_select_list():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ]

@pytest.fixture
def canceled_select_list():
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

@pytest.fixture
def one_operation_list():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}
        ]

@pytest.fixture
def sorted_in_descending_list():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]

@pytest.fixture
def sorted_in_ascending_list():
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def unselected_transactions_list() :
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
def usd_select_list() :
    return [
        {
            'id': 939719570,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
        },
        {
            'id': 142264268,
            'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'
        },
        {
            'id': 895315941,
            'state': 'EXECUTED',
            'date': '2018-08-19T04:27:37.904916',
            'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод с карты на карту',
            'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'
        },
    ]

@pytest.fixture
def rub_select_list() :
    return [
        {
            'id': 873106923,
            'state': 'EXECUTED',
            'date': '2019-03-23T01:09:46.296404',
            'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод со счета на счет',
            'from': 'Счет 44812258784861134719',
            'to': 'Счет 74489636417521191160'
        },
        {
            'id': 594226727,
            'state': 'CANCELED',
            'date': '2018-09-12T21:27:25.241689',
            'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации',
            'from': 'Visa Platinum 1246377376343588',
            'to': 'Счет 14211924144426031657'
        }
    ]

@pytest.fixture
def description_list() :
    return ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
            "Перевод с карты на карту", "Перевод организации"]

@pytest.fixture
def card_number_generated_list() :
    return ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003",
            "0000 0000 0000 0004", "0000 0000 0000 0005"]

@pytest.fixture
def matrix_gen_2_1():
    return [
        [[0, 0], [0, 1]],
        [[0, 0], [2, 1]],
        [[3, 0], [2, 1]],
        [[3, 4], [2, 1]]
        ]

@pytest.fixture
def matrix_gen_3_1():
    return [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 2], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 2], [0, 0, 3]],
        [[0, 0, 0], [0, 1, 2], [0, 4, 3]],
        [[0, 0, 0], [0, 1, 2], [5, 4, 3]],
        [[0, 0, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 0, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 8, 0], [6, 1, 2], [5, 4, 3]],
        [[7, 8, 9], [6, 1, 2], [5, 4, 3]]
        ]
