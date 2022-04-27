from typing import Generator, List, Optional, Set, Tuple

_2DList = List[List[int]]


def get(board: _2DList, row: int, col: int) -> int:
    return board[row][col]


def square(board: _2DList, row: int, col: int) -> Generator[int, None, None]:
    def calc(x: int) -> int:
        return (x // 3) * 3

    top_left_row = calc(row)
    top_left_col = calc(col)

    for row_adder in range(0, 3):
        for col_adder in range(0, 3):
            yield board[top_left_row + row_adder][top_left_col + col_adder]
    pass


def invalid(board: _2DList, row: int, col: int) -> bool:
    for iterable in (
        board[row],
        (board[r][col] for r in range(0, 9)),
        square(board, row, col),
    ):
        seen: Set[int] = set()
        for item in iterable:
            if item == 0:
                continue
            if item in seen:
                return True
            seen.add(item)
    return False


def next_coordinates(row: int, col: int) -> Optional[Tuple[int, int]]:
    if col <= 7:
        return (row, col + 1)
    if row >= 8:
        return None
    return (row + 1, 0)


def search(board: _2DList, row: int, col: int) -> bool:
    coords = (row, col)
    while coords is not None and get(board, *coords) != 0:
        coords = next_coordinates(*coords)

    if coords is None:
        return True
    row, col = coords
    next_coords = next_coordinates(*coords)

    for value in range(1, 10):
        board[row][col] = value
        if invalid(board, row, col):
            continue

        if next_coords is None or search(board, *next_coords):
            return True

    board[row][col] = 0
    return False


def solve_sudoku(board: _2DList) -> _2DList:
    return board
