import solver
import Rect

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = file.readline().replace('\n','')
    splitFirstLine = firstLine.split(' ')
    pizza = file.read().split('\n')
    solution = solver.solve(splitFirstLine[0], splitFirstLine[1], splitFirstLine[2], splitFirstLine[3], pizza)
    if (verify(pizza, solution, splitFirstLine[2], splitFirstLine[3])):
        print(evaluateSolution(pizza, solution))
    print('we failed :(')

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

    return True

def verifyRectangle(rect, pizza, minimum, maximum):
    print('give me a moment')

def evaluateSolution(pizza, solution):
    print('it\'s ok!')

readFile('pizzas/small.in')