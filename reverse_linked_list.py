def reverse_linked_list(head):
    # 2-element sliding window
    a = None
    b = head

    while b is not None:
        # save rest of the list
        old_b_next = b.next

        # reverse a -> b
        # this separates b from the rest of the list
        b.next = a

        # shift a, b forward
        a = b
        b = old_b_next

    # Note: b is guaranteed to not be None,
    # so a will be set to a non-None value.

    # loop ends when b is None,
    # so a will be that last non-None value.
    return a
