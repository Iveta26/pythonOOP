# Intro to OOP

Object Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data and code. These are contained in classes.

[A class](C:\Users\iveta_6esu9b1\PycharmProjects\calcOOP\class.png)

[We have to be careful with overriding](C:\Users\iveta_6esu9b1\PycharmProjects\calcOOP\overriding1.png)

[Overriding](C:\Users\iveta_6esu9b1\PycharmProjects\calcOOP\overriding2.png)

### Core values of OOP
1. Abstraction
2. Inheritance
3. Encapsulation
4. Polymorphism

<br />

#### 1. Abstraction
 You don't always need to know how something works to use it and still understand it.
 
```python
 cat = Animal()

# Animal class and methods like breathe are abstracted, we don't know how ir works, it's simple to understand
cat.breathe()
```

<br />

#### 2. Inheritance 
Creating new class from existing class, inherits class variables and methods.
[Visualising inheritance](C:\Users\iveta_6esu9b1\PycharmProjects\calcOOP\inheritance.png)

```python
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() # initialise the parent/base class - inherit from Animal
        self.coldBlooded = True
        self.tetrapod = None
        self.heartChambers = [3, 4]
        self.amnioticEggs = None
```

<br />

#### 3. Encapsulation
Everything is contained within a class, hiding details from users. Good at protecting important variables/objects using modifiers. Types of modifiers in python: Public(anyone), Private(__only within the class itself), Protected(_within the class and its subclasses).

```python
    def _seekHeat(self):    #underscore in front to make it protected, two to make it private
        print("it's chilly outside, I need a sunbed")
```

<br />

#### 4. Polymorphism
Methods of the same name can perform different task depending on requirements. Done by inheriting class and overriding its methods.
```python
class Animal:
    def breathe(self):
        print("One breath at a time, in and out")
```

<br />

```python
from animal import Animals

class Python(Animals):
    def breathe(self):
        print("I am breathing but I am a Python!")
```