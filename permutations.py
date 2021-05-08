import copy
from typing import List


def get_permutations(array: List[int]) -> List[int]:

    def swap(lst: List[int], i: int, j: int) -> None:
        lst[i], lst[j] = lst[j], lst[i]
        pass

    def permutations(lst: List[int], i: int, perms: List[List[int]]) -> None:
        if i == len(lst) - 1:
            # There is only 1 permutation of a single element
            perms.append(copy.deepcopy(lst))
        else:
            # rotate element at i into every position of lst[i:]
            for j in range(i, len(lst)):
                swap(lst, i, j)  # move i to j
                permutations(lst, i + 1, perms)
                swap(lst, i, j)  # restore
        pass

    perms = []
    permutations(array, 0, perms)
    return perms
