#Take a string from user as input & replace all vowels with ‘#’,
#newline with ‘|’, whitespace with ‘~’ and then display
# the new string in console.

def act1():
    myString = input("Type me some stuff: ")
    resultString = ''
    for c in myString:
        if c in "aeiouAEIOU":
            resultString += '#'
        elif c == '\n':
            resultString += '|'
        elif c in ' \t':
            resultString += '~'
        else:
            resultString += c
    print(resultString)

#Write a program to count the frequency of each word within a
# sentence taken as input from user.

def act2():
    myString = input("Type me some stuff: ")
    words = {}
    myWords = myString.split()
    for word in myWords:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for key, val in words.items():
        print(key + ": " + val)




