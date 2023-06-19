# SHOWCASING INHERITANCE

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() # initialise the parent/base class - inherit from Animal
        self.coldBlooded = True
        self.tetrapod = None
        self.heartChambers = [3, 4]
        self.amnioticEggs = None


    def _seekHeat(self):    #underscore in front to make it protected, two to make it private
        print("it's chilly outside, I need a sunbed")


    def hunt(self):
        print("Hunting prey")


    def useVenom(self):
        print("If I have it, may as well use it")

    def attractMateThroughScent(self):
        print("Time to put on the aftershave")


# greg = Reptile()
#
# greg.procreate()
# greg.useVenom()