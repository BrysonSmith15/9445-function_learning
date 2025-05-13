from typing import Callable


def run_test(function: Callable, output, args) -> bool:
    try:
        try:
            out = function(*args)
        except TypeError:
            out = function(args)
        if out != output:
            print(
                f"\x1b[0;31mThe test failed with actual output {out} and desired output {output}\x1b[0m"
            )
            return False
        else:
            # print(
            #     f"\x1b[0;32mThe test passed with outputs {out} and input {args}\x1b[0m"
            # )
            return True

    except Exception as e:
        print(
            f"\x1b[0;31mThe test threw an error: '{e}' and should have provided output {output}\x1b[0m"
        )
        return False
