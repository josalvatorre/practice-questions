def number_of_ways_to_traverse_graph(width: int, height: int):
    # horizontal distance to corner
    x = width - 1
    # vertical distance to corner
    y = height - 1
    # There need to be a certain number of right and down movements.
    # We return the number of permutations of those right and down movements.
    return factorial(x + y) // (factorial(x) * factorial(y))


def factorial(n: int) -> int:
    a = 1
    for b in range(2, n + 1):
        a *= b

    return a
