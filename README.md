# Sudoku Solver

Practice with python.
I thought it would be fun to make a sudoku solver, as it would require strong OO understanding in python.


## Usage Case
Attempts to solve sudoku puzzle. Uses row, column and box elimination techniques. Program exits when it no longer can fill in more boxes, which may be before fully solving the puzzle.
This is a commandline tool and does not contain any GUI components.


## Classes

#### Box
This represents and individual box on the sudoky board which can hold one number solution.
Tracks possibilities and alerts its three containers (row, column, square) when it knows its final answer.

#### Container
There are three types of containers: row, column, square.
Since all the types of containers function identically (they all require numbers 1-9 and contain nine boxes) they are represented by the same python class.
Alerts all boxes within itself when one box within itself has been solved.

#### Board
Contains all boxes in logical sudoku order. Contains functions to print board and is used when filling a box at some coordinate.

#### Parser
Used for parsing sudoku boards in the proper text format and filling board with starting solutions.

#### ContainerMaker
Routine for setting up boxes in proper containers.

#### Sudoku Solver
Main class for starting solver. Prints solution before exit.

## How to use
Fork this repository.
Run the following command: 
  `python3 SudokySolver.py`_`pathtoformattedsudokupuzzle`_
  
#### How to format sudoku puzzle
Check out [this file][sudoku example] for an example.

The file ending does not matter, I just used .sdku to indicate what the file is for.
Each row must be on a new line.
Empty squares must be marked as a _0_.
Columns must be seperated by a single space.

Each formatted sudoku puzzle may contain only one puzzle and may not contain anything but that puzzle.

## Created by
Noah Sragow


[sudoku example]: https://github.com/nsragow/sudoku_solver/blob/master/practice1.sdku
