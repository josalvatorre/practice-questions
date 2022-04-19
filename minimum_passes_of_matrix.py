from typing import Generator, List, Set, Tuple

IntPair = Tuple[int, int]


def minimum_passes_of_matrix(matrix: List[List[int]]) -> int:
    def neighbors(row: int, col: int) -> Generator[IntPair, None, None]:
        for row_add in range(-1, 2):
            r = row + row_add
            if r < 0 or row_count <= r:
                continue
            yield (r, col)

        for col_add in range(-1, 2):
            c = col + col_add
            if c < 0 or col_count <= c:
                continue
            yield (row, c)
        pass

    def get(row: int, col: int) -> int:
        return matrix[row][col]

    row_count = len(matrix)
    if row_count == 0:
        return 0
    col_count = len(matrix[0])

    negatives: Set[IntPair] = set()
    current_positives: Set[IntPair] = set()
    next_positives: Set[IntPair] = set()

    for row in range(row_count):
        for col in range(col_count):
            coord = (row, col)
            value = get(*coord)
            if 0 < value:
                current_positives.add(coord)
            elif value < 0:
                negatives.add(coord)
        pass

    pass_count = 0
    while len(negatives) > 0:
        flipped = False

        for coord in current_positives:
            for neighbor_coord in neighbors(*coord):
                if neighbor_coord in negatives:
                    flipped = True
                    next_positives.add(neighbor_coord)
                    negatives.remove(neighbor_coord)
        if not flipped:
            break
        pass_count += 1

        current_positives.clear()
        current_positives, next_positives = next_positives, current_positives
        pass

    return pass_count if len(negatives) == 0 else -1
