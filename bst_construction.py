from typing import NamedTuple, Optional

_LEFT = 'left'
_RIGHT = 'right'


class _ParentTarget(NamedTuple):
    parent: Optional['BST'] = None
    side: Optional[str] = None
    target: Optional['BST'] = None
    pass


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:

    @classmethod
    def find_parent_and_target(
        cls, value: int, node: 'BST',
        parent: Optional['BST'] = None, side: Optional[str] = None,
    ) -> _ParentTarget:
        # right
        if node.value < value:
            if node.right is None:
                # Could not find child, but it should have been on the right
                return _ParentTarget(parent=node, side=_RIGHT, target=None)
            else:
                # Look on right side
                return cls.find_parent_and_target(
                    value=value, node=node.right, parent=node, side=_RIGHT,
                )
        # left
        elif value < node.value:
            if node.left is None:
                # Could not find child, but it should have been on the left
                return _ParentTarget(parent=node, side=_LEFT, target=None)
            else:
                # Look on left side
                return cls.find_parent_and_target(
                    value=value, node=node.left, parent=node, side=_LEFT,
                )
        # node.value == value
        else:
            return _ParentTarget(parent=parent, side=side, target=node)

    def get_sidemost(
            self, side: str, parent: Optional['BST'] = None,
    ) -> _ParentTarget:
        self_side = getattr(self, side)
        if self_side is None:
            return _ParentTarget(parent=parent, side=side, target=self)
        return self_side.get_sidemost(side, self)

    def get_leftmost(self) -> _ParentTarget:
        return self.get_sidemost(_LEFT, None)

    def get_rightmost(self) -> _ParentTarget:
        return self.get_sidemost(_RIGHT, None)

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int) -> 'BST':
        # Write your code here.
        # Do not edit the return statement of this method.

        new_child = self.__class__(value)
        # parent and target cannot both be None
        parent, side, target = self.find_parent_and_target(value, self)

        if target is None:
            # parent and side must exist
            setattr(parent, side, new_child)
        else:
            # target.value == value
            # new_child belongs on the right of target
            if target.right is None:
                target.right = new_child
            else:
                _, _, leftmost = target.right.get_leftmost()
                leftmost.left = new_child
        return self

    def contains(self, value: int) -> bool:
        return self.find_parent_and_target(value, self).target is not None

    def remove(self, value: int) -> 'BST':
        # Write your code here.
        # Do not edit the return statement of this method.

        # parent and target cannot both be None
        parent, side, target = self.find_parent_and_target(value, self)
        if target is None:
            # node with value does not exist, so it can't be removed
            return self

        def new_subtree() -> Optional[BST]:
            """
            Returns what should replace target as child of parent.
            Manipulates the subtree to remove the element with value.
            """
            if target.left is target.right is None:
                return None
            elif target.right is not None:
                substitute_parent, substitute_side, substitute = target.right.get_leftmost()
                substitute_child = substitute.right
                if substitute_parent is None:
                    substitute_parent, substitute_side = target, _RIGHT
            else:
                substitute_parent, substitute_side, substitute = target.left.get_rightmost()
                substitute_child = substitute.left
                if substitute_parent is None:
                    substitute_parent, substitute_side = target, _LEFT
            # fill target with substitute's value
            target.value = substitute.value
            # trim the substitute from its parent
            if substitute_parent is not None:
                setattr(substitute_parent, substitute_side, substitute_child)
            return target

        if parent is None:
            # target is self is the root of the entire tree
            if target.left is target.right is None:
                # we cannot remove the root from a single-node tree
                return self
            # new_subtree() should be self
            return new_subtree()
        else:
            setattr(parent, side, new_subtree())
        return self
