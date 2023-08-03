#!/usr/bin/env python3
'''
Creates a tuple from 2 variables
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Creates a tuple from a string and value

    Args:
        k: String variable acts as key
        v: Int | Float variable acts as value

    Returns: Tuple of Key and value squared
    '''
    return (k, float(v**2))
