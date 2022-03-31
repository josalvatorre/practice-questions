from typing import List, Optional


def smallest_difference(
    array_1: List[int], array_2: List[int]
) -> Optional[List[int]]:
    if len(array_2) == 0:
        return None

    array_1.sort()
    array_2.sort()

    min_pair: Optional[List[int]] = None

    array_a, a_index = array_1, 0
    array_b, b_index = array_2, 0
    # We don't care about elements left in array b.
    # Those trailing elements can only be bigger than array_b[b_index].
    # Therefore, their absolute difference can only be bigger than
    # abs(array_a[any], array_b[-1])
    while a_index < len(array_a):
        # make sure that a <= b
        if array_a[a_index] > array_b[b_index]:
            a_index, b_index = b_index, a_index
            array_a, array_b = array_b, array_a

        pair = [array_a[a_index], array_b[b_index]]
        if array_a is not array_1:
            pair.reverse()

        min_pair = (
            pair
            if min_pair is None
            else min(
                min_pair,
                pair,
                key=lambda p: abs(p[0] - p[1]),
            )
        )

        a_index += 1
        pass

    return min_pair
