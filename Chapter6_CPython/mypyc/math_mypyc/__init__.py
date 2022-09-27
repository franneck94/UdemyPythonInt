from typing import List


def add(a: List[int], b: List[int]) -> List[int]:
    len_ = min(len(a), len(b))
    result = [0 for _ in range(len_)]
    for i in range(len_):
        result[i] = a[i] + b[i]
    return result


def clip(a: List[int], min_value: int, max_value: int) -> List[int]:
    len_ = len(a)
    for i in range(len_):
        if a[i] < min_value:
            a[i] = min_value
        elif a[i] > max_value:
            a[i] = max_value
    return a
