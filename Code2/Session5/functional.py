
def square(x):
    return x*x


def simplesummer(f, start, end):
    total = 0
    count = start
    while count <= end:
        total += f(count)
        count += 1
    return total


print(simplesummer(lambda x: x*x*x, 1, 10))

def functCuber(f, params):
    val = f(*params)
    return val*val*val

print(functCuber(lambda x, y: x+y, (2, 3)))

#write and call a function that accepts two functions and a list of parameters
#and returns the positive difference between the results of the two
#functions when applied to the same parameters

def functdif(f1, f2, args):
    f1result = f1(*args)
    f2result = f2(*args)
    return abs(f1result-f2result)

print(functdif(lambda a, b: a+b, lambda a, b: a*b, (5, 9)))