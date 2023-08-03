#!/usr/bin/env python3
'''
A function that calculate the length of a list
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes length of list

    Args:
        lst: Sequence of values

    Return: Length of list from sequence
    '''
    return [(i, len(i)) for i in lst]
