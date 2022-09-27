import numpy as np

import math_numba


def main() -> None:
    l1 = np.array([i for i in range(10)], dtype=np.int64)
    l2 = np.array([i for i in range(10)], dtype=np.int64)

    result = math_numba.add(l1, l2)
    print(result)

    min_value = 2
    max_value = 4
    math_numba.clip(l1, min_value, max_value)
    print(l1)


if __name__ == "__main__":
    main()
