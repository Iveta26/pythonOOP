# showcasing encapsulation

from reptile import Reptile #from the file reptile import class Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forkedTongue = True
        self.coldBlooded = True
        self.venom = None
        self.limbs = False
        self.tetrapod = False # overriding


    def useTongueToSmell(self):
        print("Do I say it smells nice, or it tastes nice...?")


sidney = Snake()

sidney.breathe() # Animal method
sidney._seekHeat() # Reptile method
sidney.useTongueToSmell() # Snake method