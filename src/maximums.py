from typing import List


def max_of_two(x: int, y: int):
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest: int = y
        return biggest


def max_of_three(x: int, y: int, z: int):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    int_list: List[int] = [x, y, z]
    biggest: int = x
    for i in int_list:
        if i > biggest:
            biggest: int = i
    return biggest