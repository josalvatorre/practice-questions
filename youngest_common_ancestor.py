# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def get_youngest_common_ancestor(
    top_ancestor: AncestralTree,
    descendant_1: AncestralTree,
    descendant_2: AncestralTree,
):
    """
    descendant* are leaves in the tree.
    """

    def get_depth(node: AncestralTree) -> int:
        depth = 1
        nodes = [node.name]
        while node is not top_ancestor:
            depth += 1
            node = node.ancestor
            nodes.append(node.name)
        return depth

    def youngest_ancestor(
        deeper: AncestralTree,
        other: AncestralTree,
        deeper_depth: int,
        other_depth: int,
    ) -> AncestralTree:
        # walk back up so that depth_1 == depth_2
        while deeper_depth > other_depth:
            deeper = deeper.ancestor
            deeper_depth -= 1
        # we might cross paths with other as we walk up to root
        while deeper is not other:
            deeper = deeper.ancestor
            other = other.ancestor
        return deeper

    depth_1 = get_depth(descendant_1)
    depth_2 = get_depth(descendant_2)

    if depth_1 <= depth_2:
        return youngest_ancestor(descendant_2, descendant_1, depth_2, depth_1)
    else:
        return youngest_ancestor(descendant_1, descendant_2, depth_1, depth_2)
