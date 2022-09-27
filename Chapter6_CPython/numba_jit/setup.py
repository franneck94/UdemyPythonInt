from distutils.core import setup

from math_numba import cc


def main() -> None:
    name = "math_numba"
    version = "1.0.0"
    module = cc.distutils_extension()

    setup(
        name=name,
        version=version,
        ext_modules=[module],
    )


if __name__ == "__main__":
    main()
