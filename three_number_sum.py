from typing import Callable, List, Optional, Tuple


def floored_midde(first_index: int, last_index: int):
    return (first_index + last_index) // 2


def search(
    start_index: int,
    last_index: int,
    compare: Callable[[int], int],
    return_closest: bool = False,
) -> Optional[int]:

    if last_index < start_index:
        return None

    while start_index < last_index:
        med = floored_midde(start_index, last_index)
        cmp = compare(med)

        if cmp < 0:
            # too small, go bigger
            start_index = med + 1
        elif 0 < cmp:
            # too big, go smaller
            last_index = med - 1
        else:
            return med

    # start_index == last_index now
    cmp = compare(start_index)
    if cmp == 0:
        return start_index

    if return_closest:
        return start_index
    pass


def compare(a: int, b: int) -> int:
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def three_number_sum(
    array: List[int],
    target_sum: int,
) -> List[Tuple[int, int, int]]:

    # array is now ascending
    array.sort()
    triplets = []

    for a_index in range(0, len(array) - 2):
        a = array[a_index]

        if 0 <= a_index - 1 and a == array[a_index - 1]:
            # we already saw this value
            continue

        if (
            # smallest triplet is too small
            target_sum > sum(array[a_index : a_index + 3])
            # biggest triplet is too small
            and target_sum > a + sum(array[-2:])
        ):
            continue
        elif target_sum < sum(array[a_index : a_index + 3]):
            # The smallest triplet is too big.
            # We break because a is only going to get bigger.
            break

        # k starts at biggest, keeps decreasing
        for b_index in reversed(range(a_index + 2, len(array))):
            b = array[b_index]

            if b_index + 1 < len(array) and b == array[b_index + 1]:
                # we already saw this value
                continue

            remainder = target_sum - a - b

            c_index = search(
                a_index + 1,
                b_index - 1,
                lambda i: compare(array[i], remainder),
            )
            if c_index is not None:
                triplets.append([a, array[c_index], b])

            if c_index == b_index - 1:
                # c was the biggest element between a and b.
                # Since b will only get smaller, there's no point in
                # continuing.
                break

    return triplets
