from typing import List


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstruct_bst(values: List[int]):

    def subtree(low, high, i_box):
        if len(values) <= i_box[0]:
            return None

        value = values[i_box[0]]
        if value < low or high <= value:
            return None

        # next element is either left or invalid
        i_box[0] += 1
        return BST(
            value=value,
            left=subtree(low, value, i_box),
            right=subtree(value, high, i_box))

    return subtree(float('-inf'), float('inf'), [0])
