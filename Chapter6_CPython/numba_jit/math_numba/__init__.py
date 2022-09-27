from typing import List

import numpy as np

from numba.pycc import CC


cc = CC("math_numba")
cc.verbose = True


@cc.export("add", "(i8[:], i8[:])")
def add(a: List[int], b: List[int]) -> np.ndarray:
    len_ = min(len(a), len(b))
    result = np.zeros(shape=(len_,), dtype=np.int64)
    for i in range(len_):
        result[i] = a[i] + b[i]
    return result


@cc.export("clip", "i8[:](i8[:], i8, i8)")
def clip(a: List[int], min_value: int, max_value: int) -> List[int]:
    len_ = len(a)
    for i in range(len_):
        if a[i] < min_value:
            a[i] = min_value
        elif a[i] > max_value:
            a[i] = max_value
    return a
