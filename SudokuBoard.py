class Box:

    def __init__(self):
        self.possibilities = set([1,2,3,4,5,6,7,8,9])

    @property
    def solved(self):
        if len(self.possibilities) == 1:
            return True
        else:
            return False

print("hello")

newBox = Box()

print(newBox.solved)
