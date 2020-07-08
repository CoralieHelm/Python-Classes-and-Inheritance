#July 8 2020
#20.5. Adding Other Methods to a Class

#Check Your Understanding
#Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)
        
