import math_cpp_python


def main() -> None:
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]

    l3 = math_cpp_python.add(l1, l2)
    print(l3)

    l4 = [-2, 0, 2]
    math_cpp_python.clip(l4, -1, 1)
    print(l4)


if __name__ == "__main__":
    main()
