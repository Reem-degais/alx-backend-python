#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float
"""


from typing import List, Union


mixed = Union[int, float]


def sum_mixed_list(mxd_lst: List[mixed]) -> float:
    """takes a list mxd_lst of integers and floats
    and returns their sum as a float."""
    sum_of_list = 0
    for i in mxd_lst:
        sum_of_list += i
    return (sum_of_list)
