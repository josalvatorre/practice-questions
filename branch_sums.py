from typing import List


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root) -> List[int]:
    sums: List[int] = []

    for subtree in (root.left, root.right):
        if subtree is None:
            continue
        # Add root.value to all elements in the
        # subtree's branch sums.
        sums.extend(map(lambda x: x + root.value, branch_sums(subtree)))
    # if there are no subtrees, then root.value is the branch sum.
    if len(sums) == 0:
        return [root.value]
    return sums
