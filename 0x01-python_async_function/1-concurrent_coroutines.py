#!/usr/bin/env python3

'''
Execution of multiple co-routines ansynchrously
'''

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Creates a list of co-routine delays

    Args:
        n: Number of list items
        max_delay: Max amount of seconds function delayed

    Return: List of sorted delay times
    '''
    delays = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(delays)
