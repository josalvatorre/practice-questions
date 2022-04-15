from typing import List


def search_in_sorted_matrix(matrix: List[List[int]], target: int) -> List[int]:
    if len(matrix) == 0:
        return [-1, -1]

    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and 0 <= c:
        element = matrix[r][c]

        if element < target:
            r += 1
        elif element > target:
            c -= 1
        else:
            return [r, c]
        pass
    return [-1, -1]
