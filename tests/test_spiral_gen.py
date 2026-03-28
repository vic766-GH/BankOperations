import pytest

from src.spiral_gen import spiral_generator


@pytest.mark.parametrize(
    "dimension_of_matrix, start_num, matrix_gen",
    [
        (0, 1, [[[]]]),  # корректные данные
        (1, 1, [[[1]]]),  # корректные данные
        (2, 1, "matrix_gen_2_1"),  # корректные данные
        (3, 1, "matrix_gen_3_1"),  # корректные данные
    ]
)
def test_spiral_generator(dimension_of_matrix: int, start_num: int, matrix_gen: list, request: pytest.FixtureRequest) -> None:
    if isinstance(matrix_gen, str):
        data_2 = request.getfixturevalue(matrix_gen)
    else:
        data_2 = matrix_gen

    spiral_matrix = spiral_generator(dimension_of_matrix, start_num)

    for i in range(dimension_of_matrix):
        assert next(spiral_matrix) == list(data_2[i])
