from typing import Callable, List, Optional


def search(
    first: int,
    last: int,
    compare: Callable[[int], int],
) -> Optional[int]:

    while first <= last:
        med = (first + last) // 2
        comparison = compare(med)

        if comparison < 0:
            # too small, so go right
            first = med + 1
        elif 0 < comparison:
            # too big, so go left
            last = med - 1
        else:
            return med
    return None


def search_in_sorted_matrix(matrix: List[List[int]], target: int) -> List[int]:
    def comparison(x: int):
        if x < target:
            return -1
        if target < x:
            return 1
        return 0

    if len(matrix) == 0:
        return [-1, -1]

    # start at top-right
    row_count = len(matrix)
    col_count = len(matrix[0])

    for top_right_row in range(min(row_count, col_count)):
        top_right_col = col_count - 1 - top_right_row
        top_right = matrix[top_right_row][top_right_col]

        if top_right < target:
            # search this column, which has the greater elements
            row = search(
                top_right_row,
                row_count - 1,
                lambda r: comparison(matrix[r][top_right_col]),
            )
            if row is not None:
                return [row, top_right_col]
            pass
        elif target < top_right:
            # search this row, which has the lesser elements
            col = search(
                0,
                top_right_col,
                lambda c: comparison(matrix[top_right_row][c]),
            )
            if col is not None:
                return [top_right_row, col]
            pass
        else:
            return [top_right_row, top_right_col]
        pass
    return [-1, -1]
