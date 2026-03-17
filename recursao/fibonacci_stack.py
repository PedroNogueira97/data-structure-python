def fibonacci(n):
    if n < 1:
        return 0

    stack = [n]
    memo = {1: 1, 2: 1}

    while stack:
        current = stack[-1]

        if current in memo:
            stack.pop()
            continue

        if (current - 1) in memo and (current - 2) in memo:
            memo[current] = memo[current - 1] + memo[current - 2]
            stack.pop()
        else:
            if (current - 1) not in memo:
                stack.append(current - 1)
            if (current - 2) not in memo:
                stack.append(current - 2)

    return memo[n]

print(fibonacci(5))