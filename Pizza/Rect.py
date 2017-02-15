class Rect:
    def __init__(self, left, top, right, bottom):
        if (left >= right or top >= bottom):
            raise Exception("Illegal values. left:" + str(left) + " right:" + str(right) + " top:" + str(top) + " bottom:" + str(bottom))
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def overlap(self, rect):
        return (self.left < rect.right and rect.right > self.left and self.top < rect.bottom and self.bottom > rect.top)

    def size(self):
        return (self.bottom - self.top) * (self.right - self.left)