# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_kth_largest_value_in_bst(tree, k: int):
    nodes_in_order = []

    def in_order(node):
        if node is None or k == len(nodes_in_order):
            return None
        in_order(node.right)
        nodes_in_order.append(node.value)
        in_order(node.left)

    in_order(tree)
    print(nodes_in_order)
    return nodes_in_order[k - 1]
