from typing import Callable, List, Optional, Tuple


def three_number_sum(
    array: List[int],
    target_sum: int,
) -> List[Tuple[int, int, int]]:
    def next_unique_index(
        index: int,
        advance: Callable[[int], int],
        invalid: Callable[[int], bool],
    ) -> Optional[int]:
        index, prev_index = advance(index), index
        while True:
            if invalid(index):
                return None
            if array[index] != array[prev_index]:
                return index
            index, prev_index = advance(index), index

    def next_unique_b_index(
        current_b_index: int, current_c_index: int
    ) -> Optional[int]:
        return next_unique_index(
            current_b_index,
            lambda x: x + 1,
            lambda x: current_c_index <= x,
        )

    def next_unique_c_index(
        current_b_index: int, current_c_index: int
    ) -> Optional[int]:
        return next_unique_index(
            current_c_index,
            lambda x: x - 1,
            lambda x: x <= current_b_index,
        )

    array.sort()
    triplets = []

    for a_index in range(0, len(array) - 2):
        a = array[a_index]

        if 1 <= a_index and a == array[a_index - 1]:
            # we already saw this value
            continue

        b_index = a_index + 1
        c_index = len(array) - 1
        while (
            b_index is not None and c_index is not None and b_index < c_index
        ):
            b = array[b_index]
            c = array[c_index]

            current_sum = a + b + c

            if current_sum < target_sum:
                # too small, go bigger
                b_index = next_unique_b_index(b_index, c_index)
            elif target_sum < current_sum:
                # too big, go smaller
                c_index = next_unique_c_index(b_index, c_index)
            else:
                triplets.append([a, b, c])
                b_index = next_unique_b_index(b_index, c_index)
                if b_index is None:
                    break
                c_index = next_unique_c_index(b_index, c_index)

    return triplets
