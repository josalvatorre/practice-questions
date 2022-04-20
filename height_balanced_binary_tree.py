from typing import Any, Generator


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    pass


def is_none(x: Any) -> bool:
    return x is None


def children(tree: BinaryTree) -> Generator[BinaryTree, None, None]:
    return (child for child in (tree.left, tree.right) if child is not None)


def height_balanced_binary_tree(tree: BinaryTree) -> bool:

    kids = tuple(children(tree))
    if len(kids) == 0:
        return True
    if len(kids) == 1:
        return len(tuple(children(kids[0]))) == 0

    return all(map(height_balanced_binary_tree, kids))
