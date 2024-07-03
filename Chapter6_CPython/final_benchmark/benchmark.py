"""Test code."""

import array
from typing import Any

import math_cpp_python
import math_cpython
import math_cython
import numpy as np


LIST = [float(i) for i in range(100_000)]
NP_ARRAY = np.array([float(i) for i in range(100_000)], dtype=np.float64)
PY_ARRAY = array.array("f", [float(i) for i in range(100_000)])

NUM_ROUNDS = 50
NUM_ITERATIONS = 100


# def test_python_clip(benchmark: Any) -> None:
#     benchmark.pedantic(
#         math_cython.python_clip_vector,
#         args=(LIST, -1.0, 1.0, LIST),
#         rounds=NUM_ROUNDS // 10,
#         iterations=NUM_ITERATIONS,
#     )


# def test_naive_cython_clip(benchmark: Any) -> None:
#     benchmark.pedantic(
#         math_cython.naive_cython_clip_vector,
#         args=(PY_ARRAY, -1.0, 1.0, PY_ARRAY),
#         rounds=NUM_ROUNDS // 10,
#         iterations=NUM_ITERATIONS,
#     )


def test_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.cython_clip_vector,
        args=(PY_ARRAY, -1.0, 1.0, PY_ARRAY),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_np_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        np.clip,
        args=(NP_ARRAY, -1.0, 1.0, NP_ARRAY),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


# def test_numba_clip(benchmark: Any) -> None:
#     benchmark.pedantic(
#         math_numba.clip_vector,
#         args=(NP_ARRAY, -1.0, 1.0),
#         rounds=NUM_ROUNDS,
#         iterations=NUM_ITERATIONS,
#     )


def test_cpython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpython.clip_vector,
        args=(LIST, -1.0, 1.0),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cpp_python_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpp_python.clip_vector,
        args=(LIST, -1.0, 1.0),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


# def test_mypyc_clip(benchmark: Any) -> None:
#     benchmark.pedantic(
#         math_mypyc.clip_vector,
#         args=(LIST, -1.0, 1.0),
#         rounds=NUM_ROUNDS // 4,
#         iterations=NUM_ITERATIONS,
#     )
