"""Test code.
"""
import array
from typing import Any

import numpy as np

import math_cpp_python
import math_cpython
import math_cython
import math_mypyc
import math_numba


LIST = [i for i in range(100_000)]
ARRAY = np.array([i for i in range(100_000)], dtype=np.int64)
ARRAY_ = array.array("f", [i for i in range(100_000)])

NUM_ROUNDS = 20
NUM_ITERATIONS = 100


def test_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.cython_clip_vector,
        args=(ARRAY_, -1, 1, ARRAY_),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_np_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        np.clip,
        args=(ARRAY, -1, 1, ARRAY),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_numba_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_numba.clip_vector,
        args=(ARRAY, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cpython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpython.clip_vector,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cpp_python_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpp_python.clip_vector,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_mypyc_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_mypyc.clip_vector,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS // 4,
        iterations=NUM_ITERATIONS,
    )
