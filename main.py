def factorial(n):
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r


factorial(3)
factorial(4)
factorial(factorial(3))

