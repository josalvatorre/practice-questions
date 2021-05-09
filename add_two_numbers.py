# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(None)
    current = head
    prev = None
    carry = 0

    while l1 is not None and l2 is not None:
        sum_ = l1.val + l2.val + carry
        current.val = digit = sum_ % 10
        carry = (sum_ - digit) // 10

        l1 = l1.next
        l2 = l2.next
        prev = current
        current.next = ListNode(None)
        current = current.next

    # Swap to ensure that l2 was the longer number.
    # Otherwise, we'd have to write duplicate code for both cases.
    if l2 is None:
        l1, l2 = l2, l1

    while l2 is not None:
        sum_ = l2.val + carry
        current.val = digit = sum_ % 10
        carry = (sum_ - digit) // 10

        l2 = l2.next
        prev = current
        current.next = ListNode(None)
        current = current.next

    if carry > 0:
        current.val = carry
    else:
        prev.next = None
    return head
