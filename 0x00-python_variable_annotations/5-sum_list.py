#!/usr/bin/env python3
"""Function sum_list which takes a list input_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns their sum as a float"""
    i: float = 0.0
    for input in input_list:
        i = i + input
    return i
