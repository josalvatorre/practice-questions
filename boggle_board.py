from typing import Dict, Generator, List, Set, Tuple, Union

StringBoard = List[List[str]]
TrieType = Dict[Union[str, bool], Union[Dict, str]]


def trie(strings: List[str]) -> TrieType:
    trie_ = {}

    for string in strings:
        if len(string) == 0:
            continue

        parent = trie_

        for char in string:
            entry = parent.get(char)
            if entry is None:
                entry = {}
                parent[char] = entry
            parent = entry
        parent[True] = string

    return trie_


def get(board: StringBoard, row: int, col: int) -> str:
    return board[row][col]


def boggle_board(board: StringBoard, words: List[str]) -> List[str]:
    """
    TODO speed up by destroying trie paths that already lead to a word.
    """

    def in_bounds(coords: Tuple[int, int]) -> bool:
        for value, hi_bound in zip(
            coords,
            (row_count, col_count),
        ):
            if value < 0 or hi_bound <= value:
                return False
        return True

    def neighbors(
        row: int, col: int
    ) -> Generator[Tuple[int, int], None, None]:
        for row_adder in range(-1, 2):
            for col_adder in range(-1, 2):
                if row_adder == col_adder == 0:
                    continue

                coords = (row + row_adder, col + col_adder)
                if in_bounds(coords):
                    yield coords
        pass

    def collect_words_at(
        row: int, col: int, trie_entry: Union[TrieType, str]
    ) -> None:
        this_coord = (row, col)
        current_path.add(this_coord)

        word = trie_entry.get(True)
        if word is not None:
            words_seen.add(word)

        for coord in neighbors(row, col):
            if coord in current_path:
                continue

            neighbor_char = get(board, *coord)
            neighbor_entry = trie_entry.get(neighbor_char)
            if neighbor_entry is not None:
                collect_words_at(*coord, neighbor_entry)

        current_path.remove(this_coord)
        pass

    row_count = len(board)
    if row_count == 0:
        return []
    col_count = len(board[0])

    words_trie = trie(words)
    words_seen: Set[str] = set()
    current_path: Set[Tuple[int, int]] = set()

    for row in range(row_count):
        for col in range(col_count):
            first_entry = words_trie.get(get(board, row, col))
            if first_entry is not None:
                collect_words_at(row, col, first_entry)
            pass

    return list(words_seen)
