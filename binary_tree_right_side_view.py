from typing import List, NamedTuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def right_side_view(root: TreeNode) -> List[int]:
    class Left(NamedTuple):
        node: TreeNode
        height: int

    rights: List[int] = []
    left_stack: List[Left] = []

    current_height = 0

    # Simulate a do-while loop.
    first_iteration = True

    while root is not None or first_iteration:
        first_iteration = False

        while root is not None:
            # Only add to rights if root is below the current farthest right.
            if current_height > len(rights) - 1:
                rights.append(root.val)

            # We must search the left eventually.
            if root.left is not None:
                left_stack.append(
                    Left(node=root.left, height=current_height + 1)
                )

            # Advance
            root = root.right
            current_height += 1

        if len(left_stack) > 0:
            left = left_stack.pop()
            root = left.node
            current_height = left.height

    return rights
