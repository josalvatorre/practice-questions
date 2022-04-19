from typing import List

_2DList = List[List[int]]


def get(matrix: _2DList, row: int, col: int) -> int:
    return matrix[row][col]


def set_(matrix: _2DList, value: int, row: int, col: int) -> None:
    matrix[row][col] = value
    pass


def river_sizes(matrix: _2DList) -> List[int]:
    def neighbors(row: int, col: int):
        neighbor = [row, col]
        for coord_index, upper_bound in zip(
            range(2),
            (row_count, col_count),
        ):
            original_value = neighbor[coord_index]

            for adder in (-1, 1):
                neighbor[coord_index] += adder
                if 0 <= neighbor[coord_index] < upper_bound:
                    yield tuple(neighbor)
                neighbor[coord_index] = original_value
        pass

    def river_size(row: int, col: int):
        next_squares = {(row, col)}

        size = 0
        while len(next_squares) > 0:
            square = next(iter(next_squares))
            size += 1

            for neighbor in neighbors(*square):
                if get(matrix, *neighbor) == 1:
                    next_squares.add(neighbor)

            next_squares.remove(square)
            set_(matrix, 0, *square)
            pass

        return size

    row_count = len(matrix)
    if row_count == 0:
        return []
    col_count = len(matrix[0])

    river_sizes = []

    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] == 1:
                river_sizes.append(river_size(i, j))

    return river_sizes
