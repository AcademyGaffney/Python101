def displayWelcome(name):
    if type(name) == str:
        print("Hello {}!".format(name))


displayWelcome("Mike")
displayWelcome(5)
displayWelcome([2,3,4,"we"])

dW = displayWelcome

dW("Sarah")

dW(dW)

def doubleSquare(num):
    return 2 * num

print(doubleSquare("Hi!"))

def quickFunct():
    return 1,2,3

a, b, c = quickFunct()

print(b)