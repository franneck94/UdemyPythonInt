from setuptools import Extension
from setuptools import setup


EXTENSIONS = [Extension(name="math_cpython", sources=["math_cpython/clip.c"])]


def main() -> None:
    setup(name="math_cpython", version="1.0.0", ext_modules=EXTENSIONS)


if __name__ == "__main__":
    main()
