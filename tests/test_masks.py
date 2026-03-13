import pytest

# from conftest import card_number_data, card_account_data
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, mask_card_number', [
    ('7000792289606361', '7000 79** **** 6361'), # корректные данные
    ("", ""), # некорректные данные - пустая строка
    ("700079228966361", ""), # некорректные данные - короткая строка - менее 16 символов
    ('70007922896O6361', ""), # некорректные данные - присутствует не цифра - вместо 0 - O
])
# @pytest.mark.parametrize('card_number, mask_card_number', card_number_data)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize('account, mask_account', [
    ('73654108430135874305', '**4305'),  # корректные данные
    ("", ""), # некорректные данные - пустая строка
    ("736541084301358", ""), # некорректные данные - короткая строка - менее 20 символов
    ('70007922896O6361', ""),  # некорректные данные - присутствует не цифра - вместо 0 - O
])
# @pytest.mark.parametrize('account, mask_account', card_account_data)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account