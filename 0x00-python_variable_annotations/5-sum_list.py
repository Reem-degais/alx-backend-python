#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes
a list input_list of floats as argument and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """akes a list input_list of floats as argument and
    returns their sum as a float."""
    sum_of_list = 0
    for i in input_list:
        sum_of_list += i

    return (sum_of_list)
