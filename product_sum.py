from typing import List


# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def product_sum(array: List):
    def product_sum_(lst: List, depth: int) -> int:
        psum = 0

        for x in lst:
            if isinstance(x, list):
                x_depth = depth + 1
                psum += x_depth * product_sum_(x, x_depth)
            else:
                psum += x

        return psum

    return product_sum_(array, 1)
