#!/usr/bin/env python3
""" function sum_mixed_list which takes a list mxd_lst of integers and floats"""


from typing import Union

def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    return sum(mxd_lst)
