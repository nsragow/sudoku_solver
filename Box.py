class Box:

    def __init__(self):
        self.possibilities = set([1,2,3,4,5,6,7,8,9])
        self.containers = []
    def __init__(self,printable):
        self.possibilities = set([1,2,3,4,5,6,7,8,9])
        self.containers = []
        self.printable = printable
    def add_container(self,container):
        if len(self.containers) == 3:
            raise Exception("Tried to associate another container when this box is already associated with three containers")
        else:
            self.containers.append(container)

    def fill(self, num):
        if num not in self.possibilities:
            raise Exception("tried to fill this box with %d when %d was not a possibility" % (num,num))
        else:
            leftovers = list(self.possibilities)
            for pos in leftovers:
                if pos is not num:
                    self.strike(pos)



    @property
    def solved(self):
        if len(self.possibilities) == 1:
            return True
        else:
            return False
    @property
    def answer(self):
        if not self.solved:
            raise Exception("requesting solution when box is not solved")
        else:
            for num in self.possibilities:
                return num
    def state(self):
        try:
            return self.answer
        except:
            return 0
    def strike(self, num):
        if num in self.possibilities:
            if len(self.possibilities) != 1:
                self.possibilities.remove(num)
                if self.solved:
                    #print("FOUND SOLUTION")
                    #print(self.answer)
                    #print(self.printable)
                    for container in self.containers:
                        container.found(self.answer)
