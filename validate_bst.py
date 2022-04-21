from dataclasses import dataclass
from typing import Optional


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    pass


@dataclass
class TreeInfo:
    maximum: int
    minimum: int
    pass


def validate_bst(tree: BST) -> bool:
    def tree_info(node: BST) -> Optional[TreeInfo]:

        info = TreeInfo(maximum=node.value, minimum=node.value)

        if node.left is not None:
            left = tree_info(node.left)
            if left is None or not left.maximum < node.value:
                return None
            info.minimum = left.minimum

        if node.right is not None:
            right = tree_info(node.right)
            if right is None or not node.value <= right.minimum:
                return None
            info.maximum = right.maximum

        return info

    return tree_info(tree) is not None
