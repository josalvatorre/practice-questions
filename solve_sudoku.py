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
        iterable = list(iterable)
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
    print(f"{row = } {col = }")

    coords = (row, col)
    while coords is not None and get(board, *coords) != 0:
        coords = next_coordinates(*coords)

    if coords is None:
        return True
    row, col = coords
    next_coords = next_coordinates(*coords)

    for value in range(1, 10):
        board[row][col] = value
        print(f"board[{row}][{col}] = {board[row][col]}")
        if invalid(board, row, col):
            continue

        if next_coords is None or search(board, *next_coords):
            return True
        print(f"{row = } {col = } back from failed recurse")
    board[row][col] = 0

    print(f"{row = } {col = } returning False")
    return False


def solve_sudoku(board: _2DList) -> _2DList:
    print(search(board, 0, 0))
    return board


result = solve_sudoku(
    [
        [0, 0, 0, 0, 3, 0, 0, 0, 9],
        [0, 4, 0, 5, 0, 0, 0, 7, 8],
        [2, 9, 0, 0, 0, 1, 0, 5, 0],
        [0, 7, 8, 0, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 6, 0, 0, 8, 0],
        [6, 0, 0, 8, 0, 0, 9, 3, 0],
        [0, 6, 0, 9, 0, 0, 0, 2, 7],
        [7, 2, 0, 0, 0, 5, 0, 6, 0],
        [8, 0, 0, 0, 7, 0, 0, 0, 0],
    ]
)
print("\n".join(map(str, result)))
