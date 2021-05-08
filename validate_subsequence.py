from typing import List


def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    if len(sequence) > len(array):
        return False
    a = 0
    s = 0
    while a < len(array):
        # We found matches in all of sequence.
        if len(sequence) == s:
            return True
        # We have a match. Let's advance on sequence.
        elif array[a] == sequence[s]:
            s += 1
        a += 1
    return s == len(sequence)
