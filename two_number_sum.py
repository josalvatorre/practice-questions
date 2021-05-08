from typing import List, Optional


def two_number_sum(array: List[int], target_sum: int) -> List[int]:
    # ensure that array is ascending
    array.sort()

    def find_sum(i: int, j: int) -> Optional[List[int]]:
        sum_ = array[i] + array[j]
        # i should be less than j
        if i >= j:
            return []
        elif sum_ == target_sum:
            return [array[i], array[j]]
        elif sum_ < target_sum:
            # increase sum_ by increasing i
            return find_sum(i + 1, j)
        else:
            # decrease sum_ by decreasing j
            return find_sum(i, j - 1)

    return find_sum(0, len(array) - 1)
