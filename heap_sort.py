from typing import List


def heap_sort(array: List[int]) -> List[int]:
    """
    sorts array in ascending order
    """

    def swap(buffer: List[int], a: int, b: int) -> None:
        buffer[a], buffer[b] = buffer[b], buffer[a]
        pass

    def left_child(i: int) -> int:
        """
        0 1 2 3 4 5 6
        0 -> 1 2
        1 -> 3 4
        2 -> 4 5
        """
        return i * 2 + 1

    def right_child(i: int) -> int:
        return left_child(i) + 1

    def parent(i: int) -> int:
        """
        refer to left_child
        0 <- 1 2
        ...
        However, root is its own parent
        """
        return max(
            (i - 1) // 2,
            0,
        )

    def sift_down(buffer: List[int], heap_end: int, i: int) -> None:
        """
        buffer[:heap_end] is a max-heap.
        The root (biggest element) should be the leftmost element.
        sift element i down to its proper place
        """
        while True:
            bigger_child_i = max(
                (
                    child_index for get_child in (left_child, right_child)
                    if (child_index := get_child(i)) < heap_end
                ),
                key=lambda index: buffer[index],
                default=None,
            )
            if bigger_child_i is None:
                # We reached the end of the heap
                break
            elif buffer[i] < buffer[bigger_child_i]:
                swap(buffer, i, bigger_child_i)
                # follow the same element
                i = bigger_child_i
            else:
                # neither child is bigger,
                # so this is where element i belongs
                break
        pass

    def sift_up(buffer: List[int], i: int) -> None:
        while buffer[(parent_i := parent(i))] < buffer[i]:
            swap(buffer, parent_i, i)
            i = parent_i
        pass

    def heapify(buffer: List[int]) -> None:
        # i is the first element that is not in the heap
        for i in range(1, len(buffer)):
            sift_up(buffer, i)
        pass

    heapify(array)
    for smallest_i in reversed(range(len(array))):
        # swap the root (biggest) and a leaf (one of the smallest)
        # elements in the heap
        swap(array, 0, smallest_i)
        # Sift the new root to its proper place,
        # turning array[:smallest_i] into a heap
        sift_down(buffer=array, heap_end=smallest_i, i=0)
        # array[smallest_i:] should be sorted
    return array
