from setuptools import Extension
from setuptools import setup


def main() -> None:
    name = "math_cpython"
    version = "1.0.0"
    module = Extension(name, ["mathmodule.c"])

    setup(
        name=name,
        version=version,
        ext_modules=[module],
    )


if __name__ == "__main__":
    main()
