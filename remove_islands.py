from typing import List, Set, Tuple

IntPair = Tuple[int, int]


def remove_islands(matrix: List[List[int]]) -> List[List[int]]:
    def get(row: int, col: int) -> int:
        return matrix[row][col]

    def zerofy(row: int, col: int):
        matrix[row][col] = 0
        pass

    def neighbors(row: int, col: int):
        neighbor = [row, col]
        for coord_index, upper_bound in zip(range(2), (row_count, col_count)):
            original_value = neighbor[coord_index]

            for adder in (-1, 1):
                neighbor[coord_index] += adder
                if 0 <= neighbor[coord_index] < upper_bound:
                    yield tuple(neighbor)
                neighbor[coord_index] = original_value
        pass

    def remove_island(row: int, col: int) -> None:
        next_squares: Set[IntPair] = {(row, col)}
        explored_squares: Set[IntPair] = set()

        while len(next_squares) > 0:
            square = next(iter(next_squares))
            explored_squares.add(square)

            if square[0] in (0, row_count - 1) or square[1] in (
                0,
                col_count - 1,
            ):
                return

            for neighbor in neighbors(*square):
                if get(*neighbor) == 1:
                    if neighbor not in explored_squares:
                        next_squares.add(neighbor)

            next_squares.remove(square)
            pass

        for square in explored_squares:
            zerofy(*square)
        pass

    row_count = len(matrix)
    if row_count == 0:
        return matrix
    col_count = len(matrix[0])

    for row in range(row_count):
        for col in range(col_count):
            if matrix[row][col] == 1:
                remove_island(row, col)
            pass

    return matrix
