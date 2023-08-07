#!/usr/bin/env python3
'''
Asynchronous function that awaits a period and return wait time
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits a random number of seconds

    Args:
        max_delay: Amount of seconds to delay, max 10

    Return: Number of seconds delayed
    '''
    delay_time: float = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
