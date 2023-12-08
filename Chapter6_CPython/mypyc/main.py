import math_mypyc


def main() -> None:
    lst = list(range(10))

    min_value = 2
    max_value = 4
    math_mypyc.clip_vector(lst, min_value, max_value)

    print(lst)


if __name__ == "__main__":
    main()
