import operator
from collections import deque
from typing import Callable, List


def min_max_subarray_sum(array: List[int], k: int) -> int:
    def push(
        deq: deque,
        index: int,
        in_order: Callable[[int, int], bool],
    ) -> None:
        while k <= len(deq):
            deq.popleft()

        while 0 < len(deq) and not in_order(array[deq[-1]], array[index]):
            deq.pop()
        deq.append(index)
        pass

    def push_min_deq(index: int) -> None:
        return push(min_deq, index, operator.lt)

    def push_max_deq(index: int) -> None:
        return push(max_deq, index, operator.gt)

    min_deq = deque()
    max_deq = deque()

    for i in range(k):
        for pusher in (push_min_deq, push_max_deq):
            pusher(i)
        pass

    min_max_sum = array[min_deq[0]] + array[max_deq[0]]

    for i in range(k, len(array)):
        for pusher in (push_min_deq, push_max_deq):
            pusher(i)
        min_max_sum += array[min_deq[0]] + array[max_deq[0]]
    return min_max_sum
