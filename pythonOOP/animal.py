
#SHOWCASING ABSTRACTION
class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath at a time, in and out")


    def eat(self):
        print("eat")


    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("Onwards and upwards")


#
# # cat = Animal()
# #
# # Animal class and methods like breathe are abstracted, we don't know how ir works, it's simple to understand
# cat.breathe()