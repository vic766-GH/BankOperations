import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date

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