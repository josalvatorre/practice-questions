# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates_from_linked_list(lst: LinkedList) -> LinkedList:

    node = lst
    while node is not None:

        right = node.next
        while right is not None and node.value == right.value:
            right = right.next
            pass

        node.next = right
        node = right
        pass

    return lst
