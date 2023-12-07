#!/usr/bin/env python3
'''Given the parameters and the return values'''


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
mak = Union[Any, T]
typ = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: typ = None) -> mak:
     '''a function that gets the value'''
     if key in dct:
         return dct[key]
     else:
         return
