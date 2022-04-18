from enum import IntEnum, auto, unique
from itertools import chain, count
from typing import List, Set, Tuple

IntPair = Tuple[int, int]


@unique
class PassResult(IntEnum):
    CONTINUE = auto()
    SUCCESS = auto()
    FAILURE = auto()
    pass


def minimum_passes_of_matrix(matrix: List[List[int]]) -> int:
    row_count = len(matrix)
    if len(matrix) == 0:
        return 0
    col_count = len(matrix[0])

    def apply_pass() -> int:
        flips: Set[IntPair] = set()

        def add_if_flip(
            value_coord: IntPair,
            next_coord: IntPair,
        ):
            value = matrix[value_coord[0]][value_coord[1]]
            next_value = matrix[next_coord[0]][next_coord[1]]
            if value < 0 and next_value > 0:
                flips.add(value_coord)
            elif value > 0 and next_value < 0:
                flips.add(next_coord)
            pass

        # left to right pass
        for row in range(row_count):
            for col in range(col_count - 1):
                add_if_flip((row, col), (row, col + 1))

        # top to bottom pass
        for col in range(col_count):
            for row in range(row_count - 1):
                add_if_flip(
                    (row, col),
                    (row + 1, col),
                )

        if len(flips) == 0:
            return (
                PassResult.FAILURE
                if any(x < 0 for x in chain.from_iterable(matrix))
                else PassResult.SUCCESS
            )

        for row, col in flips:
            matrix[row][col] *= -1
        return PassResult.CONTINUE

    for pass_count in count(start=0):
        result = apply_pass()
        if result == PassResult.SUCCESS:
            return pass_count
        elif result == PassResult.FAILURE:
            return -1
