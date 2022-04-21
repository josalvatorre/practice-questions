from dataclasses import dataclass


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    pass


@dataclass
class TreeInfo:
    left_arm: int
    right_arm: int
    through_root: bool
    depth: int

    def diameter(self) -> int:
        # 1 for root
        return self.left_arm + self.right_arm + 1

    def max_arm(self) -> int:
        return max(self.left_arm, self.right_arm)

    pass


def binary_tree_diameter(tree: BinaryTree) -> int:
    def tree_info(node: BinaryTree) -> TreeInfo:
        if node is None:
            return TreeInfo(
                left_arm=0,
                right_arm=0,
                through_root=False,
                depth=0,
            )

        left_child = tree_info(node.left)
        right_child = tree_info(node.right)

        depth = max(left_child.depth, right_child.depth) + 1

        this = TreeInfo(
            left_arm=left_child.depth,
            right_arm=right_child.depth,
            through_root=True,
            depth=depth,
        )

        max_child = max(
            this,
            left_child,
            right_child,
            key=lambda child: child.diameter(),
        )
        if max_child is this:
            return this

        max_child.depth = depth
        max_child.through_root = False
        return max_child

    return tree_info(tree).diameter() - 1
