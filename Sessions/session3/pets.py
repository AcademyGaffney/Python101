

class Pet:
    def __init__(self, sound):
        self.__sound = sound

    def speak(self):
        return self.__sound


class Bird(Pet):
    def __init__(self, wingspan, sound):
        self.__wingspan = wingspan
        Pet.__init__(self, sound)

    def get_wingspan(self):
        return self.__wingspan


class Dog(Pet):
    def __init__(self, withers, sound):
        self.__withers = withers
        Pet.__init__(self, sound)

    def get_withers(self):
        return self.__withers
