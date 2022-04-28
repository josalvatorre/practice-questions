# This is the class of the input linked list.
class LinkedList:
    def __init__(self: "LinkedList", value: int) -> None:
        self.value = value
        self.next = None


def shift_linked_list(head: LinkedList, k: int) -> None:
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
    if k == 0:
        return head

    tail = head
    length = 1
    while tail.next is not None:
        tail = tail.next
        length += 1

    sign = k // abs(k)
    k = sign * (abs(k) % length)

    if k == 0:
        return head

    prev = head
    if k > 0:
        tail = head
        for _ in range(k):
            tail = tail.next
            if tail is None:
                raise Exception(f"{k = } is too large for this list")
        # tail is now k stops ahead of prev

        while tail.next is not None:
            prev = prev.next
            tail = tail.next
        # tail is now actually the tail

        new_head = prev.next
        prev.next = None
        tail.next = head
        return new_head
    else:
        prev = head
        for _ in range(abs(k) - 1):
            prev = prev.next

        new_head = prev.next
        second = new_head
        prev.next = None

        while second.next is not None:
            second = second.next

        second.next = head
        return new_head
    pass
