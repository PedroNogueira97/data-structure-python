memo = {}
def fibonacci(n):
    if n in memo: return memo[n]

    if n < 1: return 0
    if n <= 2: return 1

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(5))

