#!/usr/bin/env python3
'''
A function that returns the sum of a mixed list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    A function that adds a list of ints and floats

    Args:
        mxd_lst: A mixed list of ints and floats

    Returns: Sum of mixed list
    '''
    return float(sum(mxd_lst))
