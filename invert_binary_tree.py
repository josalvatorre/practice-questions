# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> None:
    # flip children
    tree.left, tree.right = tree.right, tree.left

    for child in (tree.left, tree.right):
        if child is not None:
            invert_binary_tree(child)
    pass
