#f(n) = f(n-1) + f(n-2)
#f(1) = 1
#f(2) = 1

def fibonacci(n):
    if n < 1: return 0
    if n <= 2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
