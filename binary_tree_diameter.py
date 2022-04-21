from dataclasses import dataclass
from itertools import chain
from typing import Tuple


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    pass


@dataclass
class TreeInfo:
    arms: Tuple[int, int]
    through_root: bool
    depth: int

    def diameter(self) -> int:
        # 1 for root
        return sum(self.arms) + 1

    def max_arm(self) -> int:
        return max(self.arms)

    pass


def binary_tree_diameter(tree: BinaryTree) -> int:
    def tree_info(node: BinaryTree) -> TreeInfo:
        if node is None:
            return TreeInfo(
                arms=(0, 0),
                through_root=False,
                depth=0,
            )

        children = tuple(map(tree_info, (node.left, node.right)))
        children_depths = tuple(child.depth for child in children)

        depth = max(children_depths) + 1

        this = TreeInfo(
            arms=children_depths,
            through_root=True,
            depth=depth,
        )

        max_child = max(
            chain([this], children),
            key=lambda child: child.diameter(),
        )
        if max_child is this:
            return this

        max_child.depth = depth
        max_child.through_root = False
        return max_child

    return tree_info(tree).diameter() - 1
