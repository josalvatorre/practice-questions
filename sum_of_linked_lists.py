from itertools import zip_longest


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def iter_linked_digits(linked_list: LinkedList):
    node = linked_list
    while node is not None:
        yield node.value
        node = node.next
    pass


def sum_of_linked_lists(list_1: LinkedList, list_2: LinkedList) -> int:
    carry = 0
    node = LinkedList(None)
    head = node

    for a, b in zip_longest(
        iter_linked_digits(list_1),
        iter_linked_digits(list_2),
        fillvalue=0,
    ):
        sum_ = a + b + carry
        node.next = LinkedList(sum_ % 10)
        node = node.next
        carry = 0 if sum_ < 10 else 1
        pass

    if carry == 1:
        node.next = LinkedList(carry)

    return head.next
