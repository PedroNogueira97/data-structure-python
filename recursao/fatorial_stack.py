import sys
import os

# Adding the root directory to sys.path to allow imports from pilhas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pilhas.stack import Stack

def factorial_stack(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    stack = Stack()

    if n == 1 or n == 0:
        return 1
    
    fact = factorial_stack(n-1)
    stack.push(n)

    while not stack.is_empty():
        fact *= stack.pop()

    return fact

if __name__ == "__main__":
    n = 6
    print(f"Factorial of {n} using stack: {factorial_stack(n)}")