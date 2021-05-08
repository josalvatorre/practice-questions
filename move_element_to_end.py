from typing import List


def move_element_to_end(array: List[int], to_move: int):
    # j = where to place the next toMove we find.
    j = len(array) - 1
    # traverse array in reverse order.
    i = 0

    while i < j:
        # Avoid swapping two toMove's.
        # Decrement j to next non-toMove value.
        while i < j and array[j] == to_move:
            j -= 1

        if array[i] == to_move:
            # Move toMove to j.
            array[i], array[j] = array[j], array[i]

        i += 1

    return array
