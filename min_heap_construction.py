import copy
from typing import List, Optional


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array: List[int]):
        # Do not edit the line below.
        self.heap = self.build_heap(array)
        self._heap = None

    @staticmethod
    def _left_child_index(i: int) -> int:
        """
        0 1 2 3 4
        0 -> 1,2
        1 -> 3,4
        2 -> 5,6
        3 -> 7,8
        """
        return i * 2 + 1

    @staticmethod
    def _right_child_index(i: int) -> int:
        return MinHeap._left_child_index(i) + 1

    @staticmethod
    def _parent_index(i: int) -> int:
        """
        right is odd, left is even.
        if child is right:
            parent = (right - 1)/2
        else:
            parent = (left - 2)/2
        """
        return max(0, (i - 1) // 2)

    def build_heap(self, array: List[int]) -> List[int]:
        self._heap = copy.deepcopy(array)
        MinHeap._heapify(self._heap, len(self._heap))
        return self._heap

    @staticmethod
    def sift_down(i: int, array: List[int], heap_end: int) -> None:
        """
        swaps a node that is bigger than its children down the heap
        """
        while True:
            # Indexes of children that are smaller than their parent.
            # These are the children that could replace the parent.
            smaller_children_indexes = sorted(
                (
                    child_i
                    for getter in (
                        MinHeap._left_child_index,
                        MinHeap._right_child_index,
                    )
                    if (
                        (child_i := getter(i)) < heap_end
                        and array[i] > array[child_i]
                    )
                ),
                key=lambda index: array[index],
            )
            if len(smaller_children_indexes) > 0:
                # take the smaller child
                smaller_i = smaller_children_indexes[0]
                # swap i and its child
                array[i], array[smaller_i] = array[smaller_i], array[i]
                # i is now at smaller_i
                # continue to sift down i
                i = smaller_i
            else:
                # There are no children that could replace the parent,
                # so this is i's rightful place.
                break
        pass

    @staticmethod
    def sift_up(i: int, array: List[int]) -> None:
        """
        swaps a node that is smaller than its parent up the heap
        """
        parent_i = MinHeap._parent_index(i)
        # no need to check that i != parent_i because
        # if so, they'll point to the same value and not be >
        while array[parent_i] > array[i]:
            array[parent_i], array[i] = array[i], array[parent_i]
            i, parent_i = parent_i, MinHeap._parent_index(parent_i)
        pass

    def peek(self) -> Optional[int]:
        return self._heap[0] if len(self._heap) > 0 else None

    def remove(self) -> Optional[int]:
        if len(self._heap) == 0:
            return None
        # swap root with last node
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # remove the (former) root
        orig_root = self._heap.pop()
        # sift the new root down to its rightful place
        self.sift_down(0, self._heap, len(self._heap))
        return orig_root

    def insert(self, value) -> None:
        self._heap.append(value)
        self.sift_up(len(self._heap) - 1, self._heap)
        pass

    @staticmethod
    def _heapify(array: List[int], heap_end: int) -> None:
        """
        array[0:heap_end] will be converted into a min-heap
        Edits the array in-place
        """
        # first element is a trivial min-heap
        # i is index of first non-heap element
        for i in range(1, heap_end):
            MinHeap.sift_up(i, array)
        pass
