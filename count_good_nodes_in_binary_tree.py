from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: "TreeNode" = None
    right: "TreeNode" = None


def good_nodes(root: TreeNode) -> int:
    def good(node: TreeNode, greatest: int) -> int:

        new_greatest = max(greatest, node.val)

        return (1 if new_greatest == node.val else 0) + sum(
            good(child, new_greatest)
            for child in (node.left, node.right)
            if child is not None
        )

    return good(root, root.val)
