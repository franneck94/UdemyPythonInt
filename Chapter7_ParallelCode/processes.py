import math
import time
from multiprocessing import Process


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
    procceses = [Process(target=is_prime, args=(n,)) for n in NUMBERS]

    start = time.perf_counter_ns()

    [p.start() for p in procceses]  # type: ignore
    [p.join() for p in procceses]  # type: ignore

    end = time.perf_counter_ns()
    print(f"time: {(end - start) / 1e09} s")

    [p.close() for p in procceses]  # type: ignore


if __name__ == "__main__":
    main()
