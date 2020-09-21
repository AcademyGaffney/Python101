
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp -1)

def powerIter(base, exp, res):
    if exp == 0:
        return res
    else:
        return powerIter(base, exp-1, res*base)

def power1(base, exp):
    return powerIter(base, exp, 1)

print(power1(2, 10))

#Fibbonacci sequence
#Fib(x) = 1: 0 or 1;  = Fib(x-1) + Fib(x-2)

def fib(x):
    if(x <= 1):
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(20))