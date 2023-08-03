#!/usr/bin/env python3
'''
A function that produces the sum of a list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Function calculates the sum of a list

    Args:
        input_list: List of Floats

    Returns: The sum of floats from a list
    '''
    return float(sum(input_list))
