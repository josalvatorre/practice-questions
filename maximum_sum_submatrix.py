from itertools import islice
from typing import Generator, List, Tuple

_2DList = List[List[int]]


def delta_windows(
    matrix: _2DList,
    row: int,
    size: int,
    col_count: int,
) -> Generator[Tuple[int, int], None, None]:

    receding_window_row = row - 1
    receding_window = sum(matrix[receding_window_row][c] for c in range(size))
    new_window_row = row + size - 1
    new_window = sum(matrix[new_window_row][c] for c in range(size))

    yield (receding_window, new_window)

    for col in range(1, col_count - size + 1):

        receding_col = col - 1
        new_col = col + size - 1

        receding_window += (
            matrix[receding_window_row][new_col]
            - matrix[receding_window_row][receding_col]
        )
        new_window += (
            matrix[new_window_row][new_col]
            - matrix[new_window_row][receding_col]
        )
        yield (receding_window, new_window)
    pass


def maximum_sum_submatrix(matrix: _2DList, size: int) -> int:
    row_count = len(matrix)
    if row_count == 0:
        return
    col_count = len(matrix[0])

    corner_sum = sum(
        sum(islice(matrix[row], 0, size)) for row in range(0, size)
    )
    matrix_sums = [None] * (col_count - size + 1)
    matrix_sums[0] = corner_sum
    max_matrix_sum = corner_sum

    current_sum = corner_sum
    for col in range(1, col_count - size + 1):
        current_sum += sum(
            # add new window, subtract receding window
            matrix[r][col + size - 1] - matrix[r][col - 1]
            for r in range(0, size)
        )
        matrix_sums[col] = current_sum
        max_matrix_sum = max(max_matrix_sum, current_sum)
        pass

    for row in range(1, row_count - size + 1):
        col = 0
        for receding, new in delta_windows(matrix, row, size, col_count):
            matrix_sums[col] += new - receding
            max_matrix_sum = max(max_matrix_sum, matrix_sums[col])
            col += 1
        pass

    return max_matrix_sum
