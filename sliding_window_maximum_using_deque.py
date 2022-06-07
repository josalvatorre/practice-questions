from collections import deque
from typing import List


def max_sliding_window(nums: List[int], window_size: int) -> List[int]:
    def push(index: int) -> None:
        while (
            0 < len(decreasing_window)
            and decreasing_window[0] < index - window_size + 1
        ):
            decreasing_window.popleft()

        while (
            0 < len(decreasing_window)
            and nums[decreasing_window[-1]] < nums[index]
        ):
            decreasing_window.pop()

        decreasing_window.append(index)
        pass

    decreasing_window = deque()

    for i in range(window_size):
        push(i)

    maxs: List[int] = [nums[decreasing_window[0]]]

    for i in range(window_size, len(nums)):
        push(i)
        maxs.append(nums[decreasing_window[0]])

    return maxs
