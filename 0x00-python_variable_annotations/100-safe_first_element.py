#!/usr/bin/env python3
"""Duck Type"""


from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe first element"""
    if lst:
        return lst[0]
    else:
        return None
