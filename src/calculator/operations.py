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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": remainder
}
    