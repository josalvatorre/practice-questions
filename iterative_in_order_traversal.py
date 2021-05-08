def iterative_in_order_traversal(tree, callback):
    prev = None
    while tree is not None:
        # if we're coming from parent
        if prev in (None, tree.parent):
            prev = tree
            # then we should try to go to the left
            if tree.left is None:
                # this is the leftmost node, so call on it
                callback(tree)
                # if possible, go to the right, else to parent
                tree = tree.parent if tree.right is None else tree.right
            else:
                tree = tree.left
        # if we're coming from the left child
        elif prev is tree.left:
            prev = tree
            # then we haven't seen this node, so call on it
            callback(tree)
            # and we should try to go to the right
            tree = tree.parent if tree.right is None else tree.right
        # if we're coming from the right child
        else:
            # then we've already seen this node, and we can only go to parent
            prev = tree
            tree = tree.parent
    pass
