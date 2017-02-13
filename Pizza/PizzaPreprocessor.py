

class PizzaPreprocessor(object):

    ''' Returns for each cell the number of possible slices that cell can be in.
    '''
    def preprocess(self, pizza, minIngredient, maxSlice):
        self.pizza = pizza
        self.minIngredient = minIngredient
        self.maxSlice = maxSlice

        for pizzaRowIndex in len(self.pizza):
            for cellIndex in len(pizzaRowIndex):


    ''' Checks if cell with `cellIndex` fits in its rectangular region around `maxSlice`.
    '''
    def counterForCellWithIndex(self, cellPos):
        squareRowIndices = range(cellPos.row - self.maxSlice, cellPos.row + self.maxSlice)
        squareColIndices = range(cellPos.col - self.maxSlice, cellPos.col + self.maxSlice)
        for pizzaRowIndex in squareRowIndices:
            for cellIndex in squareColIndices:
                self.pizza[pizzaRowIndex][cellIndex]


    ''' TODO: maybe find max slice also?
    '''
    def canHaveSlice(self, firstCellPos, secondCellPos):
        if (firstCellPos.row - secondCellPos.row)**2 + (firstCellPos.col - secondCellPos.col)**2 > self.maxSlice:
            return False

        tomatoesCount, mushroomCount = self.ingerdientCountOnMandatoryRectange(firstCellPos, secondCellPos)
        if tomatoesCount > self.minIngredient and mushroomCount > self.minIngredient:
            return True


    def ingerdientCountOnMandatoryRectange(self, firstCellPos, secondCellPos):
        tomatoesCount = 0
        mushroomCount = 0

        for row in range(min(firstCellPos.row, secondCellPos.row), max(firstCellPos.row, secondCellPos.row)):
            for col in range(min(firstCellPos.col, secondCellPos.col), max(firstCellPos.col, secondCellPos.col)):
                if self.pizza == 'T':
                    tomatoesCount += 1
                else:
                    mushroomCount += 1

        return tomatoesCount, mushroomCount

    '''Finds the largest slice between the two cell positions.
    '''
    def isSlicePossible(self, firstCellPos, secondCellPos, currentTomatoesCount, currentMushroomCount):
        if currentTomatoesCount > self.minIngredient and currentMushroomCount > self.minIngredient:
            return True


