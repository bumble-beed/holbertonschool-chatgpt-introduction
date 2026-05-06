#!/usr/bin/python3
"""
Factorial Calculator (Recursive)

This script calculates the factorial of a given non-negative integer using recursion.
Factorial of n (n!) is the product of all positive integers less than or equal to n.

Usage: python3 factorial_recursive.py <number>
Example: python3 factorial_recursive.py 5  # Outputs: 120
"""

import sys

def factorial(n):
    """
    Function description: Calculate the factorial of a non-negative integer using recursion.
    
    Parameters: n (int) - A non-negative integer.
    
    Returns: int - The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorial_recursive.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
        f = factorial(num)
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)