#!/usr/bin/env python3
'''
Creates a random number of delays and makes a list
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function creates random delays and outputs the times sorted

    Args:
        n: Number of iterations/items in list
        max_delay: Maximum delay time in seconds

    Return: Sorted delay times
    '''
    delays = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delays)
