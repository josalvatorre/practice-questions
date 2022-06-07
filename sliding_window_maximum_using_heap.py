import heapq
from typing import Any, Callable, List, NamedTuple, TypeVar

T = TypeVar("T")


class HeapElement(NamedTuple):
    x: T
    key: Callable[[T], Any]

    def __lt__(self: "HeapElement", other: "HeapElement") -> bool:
        return self.key(self.x) < other.key(other.x)

    pass


def heap_element_factory(
    key_function: Callable[[T], Any],
) -> Callable[[T], HeapElement]:
    def create_heap_element(x: T) -> HeapElement:
        return HeapElement(x=x, key=key_function)

    return create_heap_element


def max_sliding_window(nums: List[int], window_size: int) -> List[int]:
    create_heap_element = heap_element_factory(lambda index: -nums[index])
    max_indices_heap: List[HeapElement] = []

    for i in range(window_size):
        heapq.heappush(max_indices_heap, create_heap_element(i))
        pass

    maxs: List[int] = [nums[max_indices_heap[0].x]]

    for i in range(window_size, len(nums)):
        window_start = i - window_size + 1

        while (
            0 < len(max_indices_heap) and max_indices_heap[0].x < window_start
        ):
            heapq.heappop(max_indices_heap)

        heapq.heappush(max_indices_heap, create_heap_element(i))
        maxs.append(nums[max_indices_heap[0].x])

    return maxs
