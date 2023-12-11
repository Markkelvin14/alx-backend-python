#!/usr/bin/env python3


import asyncio
import random


''' Write an asynchronous coroutine that takes in an integer'''


async def wait_random(max_delay: int = 10) -> float:
    '''Generates a random number and returns it after n delay'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
