#!/usr/bin/env python3
'''
A function that retrieves first list element
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Retrive the first element from a list

    Args:
        lst: Sequence of values

    Return: First element of list, else None
    '''
    if lst:
        return lst[0]
    else:
        return None
