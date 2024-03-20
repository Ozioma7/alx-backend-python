#!/usr/bin/env python3
"""Element length"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
