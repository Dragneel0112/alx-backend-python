#!/usr/bin/env python3
'''
A function that uses a dictionary to obtain a value
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    Obtains dictionary value using a key

    Args:
        dct: Dictionary
        key: Key in the dictionary
        default: None if key does not exist

    Return: Value from dictionary related to key, else None
    '''
    if key in dct:
        return dct[key]
    else:
        return default
