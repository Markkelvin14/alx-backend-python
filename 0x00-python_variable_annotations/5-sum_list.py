#!/usr/bin/env python3


'''A module for returning the sum of a list'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''A function thst returns the sum of a list'''

    tot = 0.0
    for m in input_list:
        tot += m
    return tot
