def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

print(fibonacci(5), fibonacci(200), fibonacci(1000), fibonacci(10000))
