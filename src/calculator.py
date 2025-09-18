"""
Simple Calculator Module
This module provides basic arithmetic operations.
"""

from src.utils import validate_numbers, format_result, is_safe_division


def add(a, b):
    """
    Add two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a + b
    return format_result(result)


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (float): First number
        b (float): Second number to subtract

    Returns:
        float: Difference of a and b

    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a - b
    return format_result(result)


def divide(a, b):
    # TODO: Implement the division function here
    validate_numbers(a, b)
    result = a / b
    return format_result(result)


def main():
    """
    Simple interactive calculator for testing.
    """
    print("Simple Calculator")
    print("Available operations: add, subtract, divide")
    print("Type 'quit' to exit")

    while True:
        operation = (
            input("\nEnter operation (add/subtract/divide/quit): ").lower().strip()
        )

        if operation == "quit":
            print("Goodbye!")
            break
        # TODO: Add handling for divide operation here
        if operation not in ["add", "subtract", "divide"]:
            print("Invalid operation. Please use 'add', 'subtract' or 'divide'")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == "add":
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif operation == "subtract":
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            # TODO: Add handling for divide operation here
            elif operation == "divide":
                if is_safe_division(b):
                    result = divide(a, b)
                    print(f"Result: {a} / {b} = {result}")
                else:
                    print("Do not divide by zero")
        except ValueError:
            print("Please enter valid numbers")
        except TypeError as e:
            print(f"Error: {e}")
