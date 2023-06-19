

from calculator import Calculator

class Input(Calculator):

    def getInput(self):
        a = int(input("Enter first digit: "))
        b = int(input("Enter second digit: "))
        return a, b


doCalc = Calculator()
userInp = Input()
numbers = userInp.getInput()
doCalc.add(numbers[0], numbers[1])
doCalc.subtract(numbers[0], numbers[1])
doCalc.multiply(numbers[0], numbers[1])
doCalc.divide(numbers[0], numbers[1])