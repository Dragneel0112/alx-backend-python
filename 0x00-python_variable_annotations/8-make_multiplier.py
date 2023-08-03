#!/usr/bin/env python3
'''
Function that multiplies a float by a multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Multiplier function

    Args:
        multiplier: Float variable

    Return: Product of multilier times float
    '''
    return lambda x: x * multiplier
