import math
import time
from multiprocessing import Pool


NUMBERS = [
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in {2, 3, 5, 7, 11, 13, 17}:
        return True
    if (
        n % 2 == 0
        or n % 3 == 0
        or n % 5 == 0
        or n % 7 == 0
        or n % 11 == 0
        or n % 13 == 0
        or n % 17 == 0
    ):
        return False
    upper_limit = int(math.sqrt(n)) + 1
    return all(n % i != 0 for i in range(19, upper_limit, 2))


def main() -> None:
    start = time.perf_counter_ns()

    with Pool() as pool:
        result = pool.map(is_prime, NUMBERS)
    print(result)

    end = time.perf_counter_ns()
    print(f"Took: {(end - start) / 1e09} s")


if __name__ == "__main__":
    main()
