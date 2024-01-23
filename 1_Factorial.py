"""
Your module description
"""
def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Get user input and print the factorial of the entered non-negative integer."""
    try:
        input_number = int(input("Enter a non-negative integer: "))
        factorial_result = factorial(input_number)
        print(factorial_result)
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
