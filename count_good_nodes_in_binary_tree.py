# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    def good(node: TreeNode, greatest: int) -> int:

        new_greatest = max(greatest, node.val)

        return (1 if new_greatest == node.val else 0) + sum(
            good(child, new_greatest)
            for child in (node.left, node.right)
            if child is not None
        )

    return good(root, root.val)
