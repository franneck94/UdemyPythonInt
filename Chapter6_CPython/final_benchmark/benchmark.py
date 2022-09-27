"""Test code.
"""
from typing import Any

import numpy as np

import fastvector
import math_cpp_python
import math_cpython
import math_mypyc
import math_numba


LIST = [i for i in range(100_000)]
ARRAY = np.array([i for i in range(100_000)], dtype=np.int64)
VECTOR = fastvector.VectorND([i for i in range(100_000)], dtype=fastvector.int64)

NUM_ROUNDS = 20
NUM_ITERATIONS = 100


def test_python_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.python_clip_vector,
        args=(VECTOR, -1, 1, VECTOR),
        rounds=NUM_ROUNDS // 10,
        iterations=NUM_ITERATIONS,
    )


def test_naive_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.naive_cython_clip_vector,
        args=(VECTOR, -1, 1, VECTOR),
        rounds=NUM_ROUNDS // 4,
        iterations=NUM_ITERATIONS,
    )


def test_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.cython_clip_vector,
        args=(VECTOR, -1, 1, VECTOR),
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
        math_numba.clip,
        args=(ARRAY, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cpython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpython.clip,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cpp_python_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpp_python.clip,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_mypyc_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_mypyc.clip,
        args=(LIST, -1, 1),
        rounds=NUM_ROUNDS // 4,
        iterations=NUM_ITERATIONS,
    )
