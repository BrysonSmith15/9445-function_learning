from typing import Callable

from private.test_run import run_test


def test(function: Callable, cases: list):
    print(f"Starting new test session for function \x1b[33m{function.__name__}\x1b[0m")
    for desired, test_case in cases:
        if not run_test(function, desired, test_case):
            break

    else:
        print("You completed all of the tests!")


def testset1(function: Callable) -> None:
    test(function, [((x), (x)) for x in [5, 1290194, [1, 2, 3], [(7, 8), 9]]])


def testset2(function: Callable[[int, int], int]) -> None:
    test(function, [((x + y), (x, y)) for x in range(-10, 11) for y in range(-10, 11)])


def testset3(function: Callable[[int, int, int], bool]) -> None:
    test(
        function,
        [
            (((x // y) % z == 0), (x, y, z))
            for x in range(0, 10)
            for y in range(1, 10)
            for z in range(1, 10)
        ],
    )
