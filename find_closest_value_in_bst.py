def find_closest_value_in_bst(tree: 'BST', target: int) -> int:
    node = tree
    closest = tree.value

    while node is not None:
        if abs(target - node.value) < abs(target - closest):
            closest = node.value

        if node.value <= target:
            node = node.right
        elif target < node.value:
            node = node.left
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
