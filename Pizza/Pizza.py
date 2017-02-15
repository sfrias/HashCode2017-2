from Rect import *

class Pizza:
    def __init__(self, pizzaArray):
        self.array = pizzaArray

    def sliceArray(self, rect):
        subList = self.array[rect.top:rect.bottom]
        slice = [list[rect.left:rect.right] for list in subList]
        return Slice([item for sublist in slice for item in sublist])

    def rect(self):
        return Rect(0,0, len(self.array), len(self.array[0]))

class Slice:
    def __init__(self, sliceArray):
        self.tomatoes = sum(square == 'T' for square in sliceArray)
        self.mushrooms = sum(square == 'M' for square in sliceArray)