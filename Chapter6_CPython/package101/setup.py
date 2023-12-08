from setuptools import setup


def main() -> None:
    setup(
        name="test_package",
        version="1.0.0",
        packages=["test_package"],
    )


if __name__ == "__main__":
    main()
