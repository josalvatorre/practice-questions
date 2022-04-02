from typing import List


def move_element_to_end(array: List[int], to_move: int):

    j = len(array) - 1

    for i in reversed(range(0, len(array))):
        if array[i] == to_move:
            array[j], array[i] = array[i], array[j]
            j -= 1

    return array
