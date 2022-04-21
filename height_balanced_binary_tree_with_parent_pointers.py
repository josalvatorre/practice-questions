from typing import NamedTuple, Optional


class BinaryTree(NamedTuple):
    value: int
    left: Optional["BinaryTree"]
    right: Optional["BinaryTree"]
    pass


def find_successor(
    tree: BinaryTree,
    target: BinaryTree,
) -> Optional[BinaryTree]:

    if target.right is None:

        prev = target
        node = target.parent
        while node is not None and node.left is not prev:
            node = node.parent
            prev = prev.parent

        return node

    node = target.right
    while node.left is not None:
        node = node.left
    return node
