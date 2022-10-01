from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

CYTHON_EXTENSIONS = [
    Extension(
        name="math_cython.cython_computations",
        sources=["math_cython/cython_computations.pyx"]
    )
]

EXT_MODULES = cythonize(CYTHON_EXTENSIONS, language_level="3")


def main() -> None:
    setup(
        name="math_cython",
        version="1.0.0",
        packages=["math_cython"],
        ext_modules=EXT_MODULES,
    )


if __name__ == "__main__":
    main()
