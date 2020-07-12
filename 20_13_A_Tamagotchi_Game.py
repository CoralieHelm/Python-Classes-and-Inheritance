#July 11th 2020
#20.13. A Tamagotchi Game

############################
#Creating the class

from random import randrange


class Pet():
    boredom_decrement  =  2
    hunger_decrement = 4
    boredom_threshold = 5
    hunger_threshold = 8
    sounds = ["Miau"]

    def __init__(self, name = "Snowball"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:] #makes a copy of the sound list. This way we are able to make changes

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Happy"
        elif self.hunger > self.hunger_threshold:
            return "Hungry"
        else:
            return "Bored"

    def __str__(self):
        state = "       I am " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom - max(0, self.boredom - self.boredom_decrement)

##########################################
#Creating instances of the class

pet1 = Pet("Kitty")
print(pet1)

for mood in range(6):
    pet1.clock_tick()
    print(pet1)

pet1.feed()
pet1.hi()
pet1.teach("I am Batman!")

for word_taught in range (5):
    pet1.hi()
print(pet1)

############
