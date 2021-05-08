# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_linked_lists(head_a, head_b) -> LinkedList:

    def first_head(a, b):
        return a if a.value <= b.value else b

    def in_order(a, b):
        return (a, b) if a is first_head(a, b) else (b, a)

    head_first, head_other = in_order(head_a, head_b)
    og_head_first = head_first

    while head_first.next is not None:
        if head_first.next is first_head(
            head_first.next, head_other,
        ):
            head_first = head_first.next
        else:
            rest_first = head_first.next
            head_first.next = head_other
            head_first, head_other = head_other, rest_first
        pass
    # collect remaining items (if any)
    head_first.next = head_other

    return og_head_first
