#!/usr/bin/env python3
"""
Function returns an asyncio.Task
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Calls a randomly generated wait_time function and returns a task

    Args:
        max_delay: Maximum number of seconds function delays

    Return: An asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
