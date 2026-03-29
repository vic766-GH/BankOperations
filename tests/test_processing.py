import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_list, state_select, selected_list",
    [
        ("unsorted_list", "EXECUTED", "executed_select_list"),  # корректные данные
        ("unsorted_list", "CANCELED", "canceled_select_list"),  # корректные данные
        ("one_operation_list", "CANCELED", "empty_list"),  # некорректные данные - отсутствует заданный тип операции
        ([], "CANCELED", []),  # некорректные данные - пустые словари
        ([], "", []),  # некорректные данные - отсутствует критерий операции
    ],
)
def test_filter_by_state(input_list: list, state_select: str, selected_list: list, request: pytest.FixtureRequest) -> None:
    if isinstance(input_list, str) and isinstance(selected_list, str):
        data_1 = request.getfixturevalue(input_list)
        data_2 = request.getfixturevalue(selected_list)
    else:
        data_1 = input_list
        data_2 = selected_list
    assert filter_by_state(data_1, state_select) == data_2


@pytest.mark.parametrize(
    "input_list, descending_order, selected_list",
    [
        ("unsorted_list", True, "sorted_in_descending_list"),
        ("unsorted_list", False, "sorted_in_ascending_list"),
        ([], False, []),
    ],
)
def test_sort_by_date(input_list: list, descending_order: bool, selected_list: list, request: pytest.FixtureRequest) -> None:
    if isinstance(input_list, str) and isinstance(selected_list, str):
        data_1 = request.getfixturevalue(input_list)
        data_2 = request.getfixturevalue(selected_list)
    else:
        data_1 = input_list
        data_2 = selected_list
    assert sort_by_date(data_1, descending_order) == data_2
