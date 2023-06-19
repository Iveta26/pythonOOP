

class Dog:
    animalKind = "canine"

    def bark(self): # class function - method. Self - referring to a current class
        print(self.animalKind)
        return "woof"


# Dog.bark(Dog)

# Instantiation of a class

fido = Dog()
lassie = Dog()

fido.bark()
lassie.bark()


fido.animalKind = "Big Dog"
print(fido.animalKind) # overriding

# 4 pillars of OOP
# Encapsulation - everything is contained within a class, hiding details from users, who can access what from a class (public, private). Really good at protecting important variables/objects. Types of modifiers in python: Public(anyone), Private(only within the class itself), Protected(within the class and its subclasses)
# Abstraction - you don't always need to know how something works to use it
# Inheritance - new class from existing class, inherits class var and methods
# Polymorphism - methods can have the same name, but act differently