from Box import Box
import ContainerMaker as CMModule

class Board:
    def __init__(self):
        self.set_up_array_board()
        self.set_up_containers()
    def set_up_array_board(self):
        self.array_board = []
        for num in range(0,9):
            column = []
            for num in range(0,9):
                column.append(Box(self))
            self.array_board.append(column)
    def set_up_containers(self):
        CMModule.set_up_array_board(self.array_board)
    def __str__(self):
        return_string = ""
        for y in range(0,9):
            for x in range(0,9):
                return_string += str(self.array_board[x][y].state())
                return_string += " "
            return_string += "\n"
        return return_string
