from Box import Box

class Container:
    def __init__(self,boxes):
        if len(boxes) != 9:
            raise Exception("A container must contain 9 boxes. %d boxes were supplied")
        elif len(list(filter(lambda box : not isinstance(box,Box),boxes))) != 0:
            raise Exception("A container can only contain Box objects")
        else:
            self.boxes = boxes
            self.possibilities = set([1,2,3,4,5,6,7,8,9])
    def found(self, num):
        if num in self.possibilities:
            self.possibilities.remove(num)
            for box in self.boxes:
                box.strike(num)
