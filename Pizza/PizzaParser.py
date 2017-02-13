import solver

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = file.readline().replace('\n','')
    splitFirstLine = firstLine.split(' ')
    pizza = file.read().split('\n')
    solver.solve(splitFirstLine[0], splitFirstLine[1], splitFirstLine[2], splitFirstLine[3], pizza)

readFile('pizzas/small.in')