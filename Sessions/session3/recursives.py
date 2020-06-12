def factorial(val):
    if val <= 1:
        return 1
    return val * factorial(val -1)


print(factorial(5))

def multicaller(val1, val2, f):
    return f(val1), f(val2)

print(multicaller(4, 5, factorial))