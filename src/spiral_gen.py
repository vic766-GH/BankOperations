from typing import Generator


def spiral_generator(fn: int = 0, n: int = 5) -> Generator[tuple, None, None]:
    """Программа создания и заполнения спиральной квадратной матрицы любой размерности. Параметры вызова:
    fn - первоначальное значение числовой последовательности, n - размерность матрицы"""

    matrix = [[0] * n for _ in range(n)]
    half_n = n // 2
    x, y = half_n, half_n
    num = fn
    n_circle = 1
    circle_change = True
    corner_set = False

    for _ in range(n * n):
        matrix[y][x] = num
        yield num, matrix

        num += 1

        if n % 2 == 0:
            max_num = (n_circle * 2) * (n_circle * 2)
        else:
            max_num = (n_circle * 2 - 1) * (n_circle * 2 - 1)

        if (num - fn + 1) > max_num:
            if n % 2 == 0 and (num - fn) == 2:
                circle_change = False
            else:
                circle_change = True
                n_circle += 1
        else:
            circle_change = False

        if circle_change or not corner_set:
            if n % 2 == 0:
                upper_right_corner_x = half_n + n_circle - 1
                upper_right_corner_y = half_n - n_circle
                lower_right_corner_x = half_n + n_circle - 1
                lower_right_corner_y = half_n + n_circle - 1
                lower_left_corner_x = half_n - n_circle
                #                lower_left_corner_y = half_n + n_circle - 1
                upper_left_corner_x = half_n - n_circle
                upper_left_corner_y = half_n - n_circle
            else:
                upper_right_corner_x = half_n + (n_circle - 1)
                upper_right_corner_y = half_n - (n_circle - 1)
                lower_right_corner_x = half_n + (n_circle - 1)
                lower_right_corner_y = half_n + (n_circle - 1)
                lower_left_corner_x = half_n - (n_circle - 1)
                #                lower_left_corner_y = half_n + (n_circle - 1)
                upper_left_corner_x = half_n - (n_circle - 1)
                upper_left_corner_y = half_n - (n_circle - 1)
            corner_set = True

        if circle_change or (
            (upper_left_corner_x <= x <= upper_right_corner_x) and (upper_left_corner_y <= y <= upper_right_corner_y)
        ):
            if n % 2 == 0 and num < 4:
                dx, dy = 0, 1
            else:
                dx, dy = 1, 0
        elif (y < x) and (upper_right_corner_y <= y <= lower_right_corner_y):
            dx, dy = 0, 1
        elif n % 2 == 0 and ((lower_left_corner_x < x <= lower_right_corner_x) and (x <= y)):
            dx, dy = -1, 0
        elif n % 2 == 1 and ((lower_left_corner_x < x <= lower_right_corner_x) and (x <= y)):
            dx, dy = -1, 0
        else:
            dx, dy = 0, -1

        x, y = x + dx, y + dy


# mfn = 100
# mn = 3
#
# gen = spiral_generator(fn=mfn, n=mn)
# for i in range(mn * mn):
#     next(gen)
