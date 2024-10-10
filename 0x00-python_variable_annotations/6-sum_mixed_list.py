#!/usr/bin/env python3
"""sum_mixed_list which takes a list mxd_lst of integers and floats"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list: `list mxd_lst of integers and floats and return sum"""
    return sum(mxd_lst)
