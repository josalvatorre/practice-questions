# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_loop(head):
    n1 = head.next
    n2 = n1.next

    while n1 is not n2:
        n1, n2 = n1.next, n2.next.next

    n3 = head
    while n1 is not n3:
        n1, n3 = n1.next, n3.next
    return n1
