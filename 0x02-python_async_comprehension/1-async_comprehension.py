#!/usr/bin/env python3
'''
Using Async-generator from 0-async_generator to return list of random numbers
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''
    Produces a list of 10 random numbers

    Args: N/A

    Return: List of 10 random numbers
    '''
    return [rand async for rand in async_generator()]
