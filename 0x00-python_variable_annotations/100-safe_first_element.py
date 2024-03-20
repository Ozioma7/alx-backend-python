#!/usr/bin/env python3
"""Duck Type"""


from typing import Optional, TypeVar


T = TypeVar('T')

def safe_first_element(lst: list[T]) -> Optional[T]:
    if lst:
        return lst[0]
    else:
        return None
