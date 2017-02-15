import solver
from Rect import *
from Pizza import *

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = file.readline().replace('\n','')
    splitFirstLine = [int(param) for param in firstLine.split(' ')]
    pizza = Pizza([line for line in file.read().split('\n') if len(line) > 0])
    solution = solver.solve(splitFirstLine[0], splitFirstLine[1], splitFirstLine[2], splitFirstLine[3], pizza)
    if (verify(pizza, solution, splitFirstLine[2], splitFirstLine[3])):
        print(evaluateSolution(pizza, solution))

def verify(pizza, solution, minimum, maximum):
    if (verifyOverlap(solution) == False):
        return False

    for rect in solution:
        if (verifyRectangle(rect, pizza, minimum, maximum) == False):
            return False

    return True

def verifyOverlap(solution):
    index = 0
    secondaryIndex = 1
    while index < len(solution):
        while secondaryIndex < len(solution):
            rect1 = solution[index]
            rect2 = solution[secondaryIndex]
            if rect1.overlap(rect2):
                return False
            secondaryIndex = secondaryIndex + 1
        index = index + 1

    return True

def verifyRectangle(rect, pizza, minimum, maximum):
    size = rect.size()
    if size > maximum or size < (minimum *2):
        return False

    slice = pizza.sliceArray(rect)

    return slice.tomatoes >= minimum and slice.mushrooms >= minimum

def evaluateSolution(pizza, solution):
    solutionSize = float(sum([rect.size() for rect in solution]))
    pizzaSize = float(pizza.rect().size())
    return (solutionSize / pizzaSize) * 100

readFile('pizzas/small.in')