from typing import List


def max_subset_sum_no_adjacent(array: List[int]) -> int:
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    # sums 1st and 2nd maximal paths
    _2nd = array[0]
    _1st = max(array[0], array[1])

    for i in range(2, len(array)):
        _2nd, _1st = _1st, max(_1st, _2nd + array[i])

    return _1st
