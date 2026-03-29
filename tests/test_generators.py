import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "unselected_list, currency, selected_list",
    [
        ("unselected_transactions_list", "USD", "usd_select_list"),  # корректные данные
        ("unselected_transactions_list", "RUB", "rub_select_list"),  # корректные данные
        ("unselected_transactions_list", "CNY", "empty_list"),  # некорректные данные - отсутствует заданный тип операции
        ([], "USD", []),  # некорректные данные - пустые словари
        ([], "", []),  # некорректные данные - отсутствует критерий операции
    ],
)
def test_filter_by_currency(unselected_list: list, currency: str, selected_list: list,
    request: pytest.FixtureRequest) -> None:
    if isinstance(unselected_list, str) and isinstance(selected_list, str):
        data_1 = request.getfixturevalue(unselected_list)
        data_2 = request.getfixturevalue(selected_list)
    else:
        data_1 = unselected_list
        data_2 = selected_list

    transactions = filter_by_currency(data_1, currency)

    for i in range(len(data_1)):
        try:
            assert next(transactions) == data_2[i]
        except StopIteration:
            pass

@pytest.mark.parametrize(
    "unselected_list, selected_list",
    [
        ("unselected_transactions_list", "description_list"),  # корректные данные
        ([], []),  # некорректные данные - пустые словари
     ],
)
def test_transaction_descriptions(unselected_list: list, selected_list: list,
    request: pytest.FixtureRequest) -> None:
    if isinstance(unselected_list, str) and isinstance(selected_list, str):
        data_1 = request.getfixturevalue(unselected_list)
        data_2 = request.getfixturevalue(selected_list)
    else:
        data_1 = unselected_list
        data_2 = selected_list

    transactions = transaction_descriptions(data_1)

    for i in range(len(data_1)):
        try:
            assert next(transactions) == data_2[i]
        except StopIteration:
            pass

@pytest.mark.parametrize(
    "start_num, end_num, card_number_list",
    [
        (1, 5, "card_number_generated_list"),  # корректные данные
        (5,  5, ["0000 0000 0000 0005"]),  # корректные данные - начальный номер равен конечному
        (6, 5, []),  # некорректные данные - начальный номер больше конечного
     ],
)
def test_card_number_generator(start_num: int, end_num: int, card_number_list: list,
    request: pytest.FixtureRequest) -> None:
    if isinstance(card_number_list, str) :
        data_2 = request.getfixturevalue(card_number_list)
    else:
        data_2 = card_number_list

    card_number = card_number_generator(start_num, end_num)

    for i in range(end_num - start_num + 1):
        try:
            assert next(card_number) == data_2[i]
        except StopIteration:
            print("\nНачальный номер больше конечного")
