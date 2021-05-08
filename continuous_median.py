import operator
from typing import Callable, List


def parent(i: int) -> int:
    """
    0 -> 1 2
    1 -> 3 4
    2 -> 5 6
    """
    return max((i - 1) // 2, 0)


def left_child(i: int) -> int:
    return i * 2 + 1


def right_child(i: int) -> int:
    return left_child(i) + 1


def sift_up(heap: List[int], comes_before: Callable) -> None:
    assert 0 <= len(heap)

    i = len(heap) - 1
    while 0 < i:
        parent_i = parent(i)

        if comes_before(heap[i], heap[parent_i]):
            heap[parent_i], heap[i] = heap[i], heap[parent_i]
            parent_i, i = i, parent_i
        else:
            break
    pass


def sift_down(heap, comes_before) -> None:
    assert 0 <= len(heap)

    i = 0
    while i < len(heap):

        child_candidates = tuple(
            child for child in (left_child(i), right_child(i))
            if child < len(heap) and comes_before(heap[child], heap[i])
        )
        if len(child_candidates) == 0:
            break
        elif len(child_candidates) == 2 and comes_before(
            heap[child_candidates[1]], heap[child_candidates[0]],
        ):
            child = child_candidates[1]
        else:
            child = child_candidates[0]

        heap[child], heap[i] = heap[i], heap[child]
        child, i = i, child
    pass


def add_to_heap(number, heap, comes_before) -> None:
    heap.append(number)
    sift_up(heap, comes_before)
    pass


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # self.median is calculated.
        # self.median is either in a heap or is the average
        # of the two heap top.
        self.median = None
        # min heap of bigger half
        self.min_heap = []
        self.min_heap_comes_before = operator.lt
        # max heap of smaller half
        self.max_heap = []
        self.max_heap_comes_before = operator.gt

    def insert(self, number):

        assert abs(len(self.min_heap) - len(self.max_heap)) <= 1

        # by default, we'll add to the min heap
        heap, heap_cb, other_heap, other_heap_cb = (
            self.min_heap, self.min_heap_comes_before,
            self.max_heap, self.max_heap_comes_before,
        )
        if 0 < len(self.max_heap) and number <= self.max_heap[0]:
            heap, heap_cb, other_heap, other_heap_cb = (
                other_heap, other_heap_cb, heap, heap_cb,
            )

        add_to_heap(number, heap, heap_cb)

        # if heap is now two elements bigger, we must re-balance
        if len(other_heap)+2 == len(heap):
            heap_top = heap[0]
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            sift_down(heap, heap_cb)

            other_heap.append(heap_top)
            sift_up(other_heap, other_heap_cb)

        if len(heap) == len(other_heap):
            self.median = (heap[0] + other_heap[0]) / 2
        else:
            self.median = max((heap, other_heap), key=len)[0]
        pass

    def get_median(self):
        return self.median
