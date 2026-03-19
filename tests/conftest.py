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