#!/usr/bin/env python3
"""
Calculate the execution time of 1 co-routine function
"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Calculates total_time / n for wait_n() execution
    Which is the average (1 co-routine)

    Args:
        n: Number of items
        max_delay: Maximun delay in seconds

    Return: Total time for function to execute
    """

    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
