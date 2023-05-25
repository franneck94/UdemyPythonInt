import array

import math_cython


def main() -> None:
    lst = [float(i) for i in range(10)]
    arr1 = array.array("f", list(range(10)))
    arr2 = array.array("f", list(range(10)))

    min_value = 2.0
    max_value = 4.0
    math_cython.python_clip_vector(lst, min_value, max_value, lst)
    math_cython.naive_cython_clip_vector(arr1, min_value, max_value, arr1)
    math_cython.cython_clip_vector(arr2, min_value, max_value, arr2)

    print(lst)
    print(arr1)
    print(arr2)


if __name__ == "__main__":
    main()
