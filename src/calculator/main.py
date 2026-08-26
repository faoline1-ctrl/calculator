from .operations import *

def main():
    prev_result = None
    while True:
        if prev_result != None:
            operation_input = input(f"What would you like to do with {prev_result}?\n" 
            "(add, subtract, multiply, divide, remainder, clear, exit): ").lower()
        else:
            operation_input = input("What would you like to do? (add, subtract, multiply, divide, remainder, exit): ").lower()
        if operation_input == "exit":
            print("Goodbye!")
            break
        if operation_input == "clear":
            prev_result = None
            continue

        result = operation_setup(operation_input, prev_result)
        print(f"Result of {operation_input} is: {result}")
        prev_result = result


if __name__ == "__main__":
    main()