from collections.abc import Callable


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2

OPERATIONS: dict[str, Callable[[int, int], int | float]] = {
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "*": multiply,
    "divide": divide,
    "/": divide,
    "remainder": remainder,
    "%": remainder
}

def operation_setup(operation: str, prev_result: int | float | None = None) -> int | float | str:
    if operation not in OPERATIONS:
        return "Invalid input"

    if prev_result == None:
        num1 = int(input("Enter first number\n"))
    else:
        num1 = prev_result
    num2 = int(input("Enter second number\n"))

    return OPERATIONS[operation](num1, num2)
    