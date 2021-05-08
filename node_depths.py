from typing import Iterable


def node_depths(root) -> int:
    def child_nodes(r) -> Iterable:
        return (
            child for child in (r.left, r.right)
            if child is not None
        )

    def depths(r, depth: int) -> int:
        return depth + sum(
            depths(child, depth + 1)
            for child in child_nodes(r)
        )

    return depths(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
