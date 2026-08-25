from .operations import *

def main():
    operation_input = input("What would you like to do? (add, subtract, multiply, divide, remainder): ")

    if operation_input == "add":
        num1 = input("Enter first number\n")
        num2 = input("Enter second number\n")
        print(add(int(num1), int(num2)))
    elif operation_input == "subtract":
        num1 = input("Enter first number\n")
        num2 = input("Enter second number\n")
        print(subtract(int(num1), int(num2)))
    elif operation_input == "multiply":
        num1 = input("Enter first number\n")
        num2 = input("Enter second number\n")
        print(multiply(int(num1), int(num2)))
    elif operation_input == "divide":
        num1 = input("Enter first number\n")
        num2 = input("Enter second number\n")
        print(divide(int(num1), int(num2)))
    elif operation_input == "remainder":
        num1 = input("Enter first number\n")
        num2 = input("Enter second number\n")
        print(remainder(int(num1), int(num2)))
    else:
        return "Invalid input"


if __name__ == "__main__":
    main()