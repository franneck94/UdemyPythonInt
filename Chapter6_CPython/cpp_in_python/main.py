import math_cpp_python


def main() -> None:
    lst = [i for i in range(10)]

    min_value = 2
    max_value = 4
    math_cpp_python.clip_vector(lst, min_value, max_value)

    print(lst)


if __name__ == "__main__":
    main()
