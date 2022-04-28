# This is the class of the input linked list.
class LinkedList:
    def __init__(self: "LinkedList", value: int) -> None:
        self.value = value
        self.next = None


def shift_linked_list(head: LinkedList, k: int) -> LinkedList:
    """
    2
    0 -> 1 -> 2 -> 3 -> 4 -> 5
                   ^    ^
    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0
    0 -> 1 -> 2 -> 3    4 -> 5 -> 0

    -2
    0 -> 1 -> 2 -> 3 -> 4 -> 5
         ^    ^
    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0
    0 -> 1    2 -> 3 -> 4 -> 5
    """
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    offset = abs(k) % length
    if offset == 0:
        return head

    new_tail_index = (length - offset if k > 0 else offset) - 1
    new_tail = head
    for _ in range(new_tail_index):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
