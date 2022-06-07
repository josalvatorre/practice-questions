from copy import copy
from itertools import count
from typing import List


def max_sliding_window(nums: List[int], window_size: int) -> List[int]:
    block_max_from_left = [None] * len(nums)
    block_max_from_right = copy(block_max_from_left)

    block_count = (len(nums) // window_size) + (
        0 if len(nums) % window_size == 0 else 1
    )

    for block_i in range(block_count):
        block_start = block_i * window_size
        block_end = min(
            block_start + window_size - 1,
            len(nums) - 1,
        )

        block_range = range(block_start, block_end + 1)

        for array, rev in (
            (block_max_from_left, False),
            (block_max_from_right, True),
        ):
            iterator = reversed(block_range) if rev else iter(block_range)

            first_index = next(iterator)
            block_max = nums[first_index]
            array[first_index] = block_max

            for i in iterator:
                block_max = max(block_max, nums[i])
                array[i] = block_max
        pass

    return [
        max(block_max_from_right[a], block_max_from_left[b])
        for a, b in zip(
            count(start=0),
            range(window_size - 1, len(nums)),
        )
    ]
