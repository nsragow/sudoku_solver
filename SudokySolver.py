from Board import Board
import Parser
import sys

if len(sys.argv) < 2:
    print("Needs reference to file containing sudoku board as an argument.\nExiting...")
    sys.exit()
else:
    print("Using sudoku from file %s" % sys.argv[1])
    file = open(sys.argv[1],"r")

    board = Board()
    Parser.fill_board(file,board)
    print(board)
