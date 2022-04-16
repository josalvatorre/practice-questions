# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_node_from_end(head: LinkedList, k: int):
    def oob_exception():
        return Exception(f"{k=} is greater than the length of this list")

    second = head
    for _ in range(k):
        if second is None:
            raise oob_exception()
        second = second.next

    if second is None:
        # Then we're removing the head.
        if head.next is None:
            head.value = None
            return
        head.value = head.next.value
        head.next = head.next.next
        return

    first = head
    while second.next is not None:
        second = second.next
        first = first.next
    # first is now the (k-1)th node from the end.

    first.next = None if first.next is None else first.next.next
    pass
