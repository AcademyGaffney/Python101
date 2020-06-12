

class Pet:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound


class Bird(Pet):
    def __init__(self, wingspan, sound):
        self.wingspan = wingspan
        Pet.__init__(self, sound)

    def get_wingspan(self):
        return self.wingspan


class Dog(Pet):
    def __init__(self, withers, sound):
        self.withers = withers
        Pet.__init__(self, sound)

    def get_withers(self):
        return self.withers