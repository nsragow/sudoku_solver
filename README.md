# sudoku_solver

Practice with python.
I thought it would be fun to make a sudoku solver, as it would require strong OO understanding in python.


## usage case
Attempts to solve sudoku puzzle. Uses row, column and box elimination techniques. Program exits when it no longer can fill in more boxes, which may be before fully solving the puzzle.


## classes

#### Box
This represents and individual box on the sudoky board which can hold one number solution.
Tracks possibilities and alerts its three containers (row, column, square) when it knows its final answer.

#### Container
