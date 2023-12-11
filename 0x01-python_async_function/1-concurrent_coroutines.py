#!/usr/bin/env python3


from typing import List


''' Import wait_random from the previous python file'''


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' returns a sorted list of float numbers gotten randomly'''
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    m = 0

    while m < n:
        delay_list.append(await wait_random(max_delay))
        m += 1

    return sorted(delay_list)
