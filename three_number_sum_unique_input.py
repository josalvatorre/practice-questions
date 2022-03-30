from typing import Callable, List, Optional


def median_low(first_index: int, last_index: int) -> int:
    return (first_index + last_index) // 2


def search(
    first_index: int,
    last_index: int,
    compare: Callable[[int], int],
    return_closest: bool = False,
) -> Optional[int]:

    if last_index < first_index:
        return None

    while first_index < last_index:
        med = median_low(first_index, last_index)
        comp = compare(med)

        if 0 < comp:
            # too big so decrease
            last_index = med - 1
        elif comp < 0:
            # too small so increase
            first_index = med + 1
        else:
            return med
    # first_index == last_index now
    comp = compare(first_index)
    if comp == 0:
        return first_index

    if return_closest:
        return first_index
    return None


def compare(x: int, y: int) -> int:
    if x < y:
        return -1
    if y < x:
        return 1
    return 0


def three_number_sum(
    array: List[int],
    target_sum: int,
) -> List[List[int]]:

    array = sorted(array)
    result: List[List[int]] = []

    for a_index in range(0, len(array) - 2):
        a = array[a_index]

        def compare_to_largest_b(index: int):
            x = array[index]
            smallest_possible_sum = a + (a + 1) + x
            return compare(smallest_possible_sum, target_sum)

        largest_b_index = search(
            a_index + 1,
            len(array) - 1,
            compare_to_largest_b,
            return_closest=True,
        )
        if largest_b_index < a_index + 2:
            break

        for b_index in reversed(range(a_index + 2, largest_b_index + 1)):
            b = array[b_index]

            c_index = search(
                a_index + 1,
                b_index - 1,
                lambda i: compare(sum((a, b, array[i])), target_sum),
            )
            if c_index is not None:
                result.append([a, array[c_index], b])

    return result
