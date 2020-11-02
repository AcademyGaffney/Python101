def sumIntsIter(num):
    total = 0
    for i in range(0, num+1):
        total += i
    return total

def sumIntsRec(num):
    print("Called with " + str(num))
    if num == 0:
        return 0
    result = sumIntsRec(num-1) + num
    print("returning " + str(result))
    return result


def sumIntsTail(num):
    return sumIntsHelper(num, 0)


def sumIntsHelper(num, total):
    if num == 0:
        return 0 + total
    return sumIntsHelper(num - 1, total + num)


def sigma(funct, start, end, step = 1):
    total = 0
    for i in range(start, end+1, step):
        total += funct(i)
    return total

def square(num):
    return num ** 2

print(sigma(lambda a: a ** 3, 1, 5))

q = lambda a: a ** 3

print(q(5))