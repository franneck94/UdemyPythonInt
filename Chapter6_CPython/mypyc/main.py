import numpy as np

import math_mypyc


def main() -> None:
    l1 = [i for i in range(10)]
    l2 = [i for i in range(10)]

    result = math_mypyc.add(l1, l2)
    print(result)

    min_value = 2
    max_value = 4
    math_mypyc.clip(l1, min_value, max_value)
    print(l1)


if __name__ == "__main__":
    main()
