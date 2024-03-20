#!/usr/bin/env python3
"""String and Int to Tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing the key and the square of the value."""
    return (k, float(v ** 2))
