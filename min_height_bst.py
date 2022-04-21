from typing import Generator, List, Optional


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    pass


def min_height_bst(array: List[int]) -> Optional[BST]:
    def pre_order_traversal(
        start: int,
        end: int,
    ) -> Generator[int, None, None]:
        if end < start:
            return

        mid = (start + end) // 2
        yield array[mid]
        yield from pre_order_traversal(start, mid - 1)
        yield from pre_order_traversal(mid + 1, end)
        pass

    if len(array) == 0:
        return None

    elements = pre_order_traversal(0, len(array) - 1)
    tree = BST(next(elements))
    for e in elements:
        tree.insert(e)
    return tree
