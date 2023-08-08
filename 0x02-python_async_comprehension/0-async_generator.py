#!/usr/bin/env python3
'''
Async Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronous functions that generates random numbers

    Args: N/A

    Return: Returns random floats after co-routine sleeps for 1 second
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
