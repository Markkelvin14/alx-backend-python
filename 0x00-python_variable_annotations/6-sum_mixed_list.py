#!/usr/bin/env python3


'''A python module that which takes a list mxd_lst of integers and floats'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''a type_annotated function that returns float sum of mxd_lst'''

    tot = 0.00
    for m in mxd_lst:
        tot += m
    return tot
