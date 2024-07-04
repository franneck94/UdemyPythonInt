from Cython.Build import cythonize
from setuptools import Extension
from setuptools import setup


CYTHON_EXTENSIONS = [
    Extension(
        name="math_cython.cython_computations",
        sources=["math_cython/cython_computations.pyx"],
        extra_compile_args=["/openmp"],
        extra_link_args=["/openmp"],
    ),
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
