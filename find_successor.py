from typing import NamedTuple, Optional


# This is an input class. Do not edit.
class BinaryTree(NamedTuple):
    value: int
    left: Optional["BinaryTree"]
    right: Optional["BinaryTree"]
    parent: Optional["BinaryTree"]


def in_order_traversal(tree: BinaryTree):
    if tree is None:
        return

    yield from in_order_traversal(tree.left)
    yield tree
    yield from in_order_traversal(tree.right)
    pass


def find_successor(tree: BinaryTree, target: BinaryTree):

    nodes = in_order_traversal(tree)

    while True:
        node = next(nodes)
        if node is target:
            return next(nodes, None)

    return None
