import Session3.pets as p

petstore = []

petstore.append(p.Dog(35, "woof"))
petstore.append(p.Dog(25, "aroo"))
petstore.append(p.Bird(20, "tweet"))
petstore.append(p.Bird(30, "SQUAWK"))
petstore.append(p.Bird(90, "CAW"))

for pet in petstore:
    print(pet.speak())


def bird_stats(petlist):
    birds = 0
    wings = 0
    for pet in petlist:
        if type(pet) == p.Bird:
            birds += 1
            wings += pet.get_wingspan()
    return birds, wings/birds

print(bird_stats(petstore))
