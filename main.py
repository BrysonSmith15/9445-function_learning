def my_function(args): ...


def my_function2(arg1: int, arg2: int) -> int: ...


def myfunction3(arg1: int, arg2: int, arg3: int) -> bool: ...


if __name__ == "__main__":
    from private.tests import testset1, testset2, testset3

    testset1(my_function)
    testset2(my_function2)
    testset3(myfunction3)
