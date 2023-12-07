#!/usr/bin/env python3


'''Annotating the below function’s parameters'''


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Annotating the function parameters'''
    return [(i, len(i)) for i in lst]
