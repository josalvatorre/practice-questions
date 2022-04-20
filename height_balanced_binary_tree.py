from typing import Optional, Tuple


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    pass


def children(
    tree: BinaryTree,
) -> Tuple[Optional[BinaryTree], Optional[BinaryTree]]:
    return (tree.left, tree.right)


def max_height_or_unbalanced(tree: BinaryTree) -> Optional[int]:
    if tree is None:
        return 0

    heights = tuple(map(max_height_or_unbalanced, children(tree)))
    if len(heights) == 0:
        return 1
    if any(h is None for h in heights) or abs(heights[0] - heights[1]) > 1:
        return None
    return 1 + max(heights)


def height_balanced_binary_tree(tree: BinaryTree) -> bool:
    return max_height_or_unbalanced(tree) is not None
