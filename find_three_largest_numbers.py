from typing import List, Optional


def find_three_largest_numbers(array):
    top_size = 3

    if len(array) < top_size:
        return None

    def update_top(top_nums: List[Optional[int]], x: int) -> None:
        # xi will be the index where x should be inserted
        # or -1
        xi = len(top_nums) - 1
        while 0 <= xi and (top_nums[xi] is not None and x < top_nums[xi]):
            xi -= 1

        # shift and update
        for i in range(xi + 1):
            if i == xi:
                top_nums[i] = x
            else:
                top_nums[i] = top_nums[i + 1]

    # get the first 3
    top = [None] * top_size

    for n in array:
        update_top(top, n)

    return top
