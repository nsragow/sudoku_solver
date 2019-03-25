from Board import Board

def line_to_list(line):
    return line.split()
def parse(file):
    double_array = []
    for i in range(0,9):
        double_array.append([])

    for i in range(0,9):
        row = file.readline().split()
        for x in range(0,9):
            double_array[x].append(int(row[x]))
    return double_array



def fill_board(file,board):
    double_array = parse(file)

    coordinates = [(x,y) for x in range(0,9) for y in range(0,9)]
    for coor in coordinates:
        if double_array[coor[0]][coor[1]] != 0:
            board.array_board[coor[0]][coor[1]].fill(double_array[coor[0]][coor[1]])



# print(parse(open("./practice1.sdku","r")))
