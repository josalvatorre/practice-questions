from typing import List


def spiral_traverse(array: List[List[int]]) -> List[int]:
    top_row = 0
    bottom_row = len(array) - 1

    left_col = 0
    right_col = len(array[0]) - 1

    spiral = []
    while top_row <= bottom_row and left_col <= right_col:
        # top slice
        spiral.extend(array[top_row][left_col : right_col + 1])

        # right slice
        # do not double-count the corners
        for row in range(top_row + 1, bottom_row):
            spiral.append(array[row][right_col])

        # bottom slice
        # do not double-count if there is only one row
        if bottom_row != top_row:
            spiral.extend(
                array[bottom_row][
                    right_col : left_col - len(array[bottom_row]) - 1 : -1
                ]
            )

        # left slice
        # do not double-count the corners
        if left_col != right_col:
            for row in range(bottom_row - 1, top_row, -1):
                spiral.append(array[row][left_col])

        top_row += 1
        bottom_row -= 1

        left_col += 1
        right_col -= 1

    return spiral
