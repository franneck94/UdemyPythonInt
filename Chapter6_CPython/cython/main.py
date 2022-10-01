import array

import math_cython


def main() -> None:
    lst = [float(i) for i in range(10)]
    arr = array.array("f", [i for i in range(10)])

    min_value = 2.0
    max_value = 4.0
    math_cython.python_clip_vector(lst, min_value, max_value, lst)
    math_cython.naive_cython_clip_vector(arr, min_value, max_value, arr)
    math_cython.cython_clip_vector(arr, min_value, max_value, arr)

    print(lst)
    print(arr)


if __name__ == "__main__":
    main()
