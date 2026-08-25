from .operations import *

def main():
    operation_input = input("What would you like to do? (add, subtract, multiply, divide, remainder): ")
    result = operation_setup(operation_input)
    print(f"Result of {operation_input} is: {result}")


if __name__ == "__main__":
    main()