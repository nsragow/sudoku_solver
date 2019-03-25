from Container import Container


row_addresses = []
column_addresses = []
square_addresses = []

for y in range(0,9):
    some_row = []
    for x in range(0,9):
        some_row.append((x,y))
    row_addresses.append(some_row)
for x in range(0,9):
    some_column = []
    for y in range(0,9):
        some_column.append((x,y))
    column_addresses.append(some_column)

#square 1
some_square = []
some_square.append((0,0))
some_square.append((0,1))
some_square.append((0,2))

some_square.append((1,0))
some_square.append((1,1))
some_square.append((1,2))

some_square.append((2,0))
some_square.append((2,1))
some_square.append((2,2))
square_addresses.append(some_square)

#square 2
some_square = []
some_square.append((3,0))
some_square.append((3,1))
some_square.append((3,2))

some_square.append((4,0))
some_square.append((4,1))
some_square.append((4,2))

some_square.append((5,0))
some_square.append((5,1))
some_square.append((5,2))
square_addresses.append(some_square)

#square 3
some_square = []
some_square.append((6,0))
some_square.append((6,1))
some_square.append((6,2))

some_square.append((7,0))
some_square.append((7,1))
some_square.append((7,2))

some_square.append((8,0))
some_square.append((8,1))
some_square.append((8,2))
square_addresses.append(some_square)

#square 4
some_square = []
some_square.append((0,3))
some_square.append((0,4))
some_square.append((0,5))

some_square.append((1,3))
some_square.append((1,4))
some_square.append((1,5))

some_square.append((2,3))
some_square.append((2,4))
some_square.append((2,5))
square_addresses.append(some_square)

#square 5
some_square = []
some_square.append((3,3))
some_square.append((3,4))
some_square.append((3,5))

some_square.append((4,3))
some_square.append((4,4))
some_square.append((4,5))

some_square.append((5,3))
some_square.append((5,4))
some_square.append((5,5))
square_addresses.append(some_square)

#square 6
some_square = []
some_square.append((6,3))
some_square.append((6,4))
some_square.append((6,5))

some_square.append((7,3))
some_square.append((7,4))
some_square.append((7,5))

some_square.append((8,3))
some_square.append((8,4))
some_square.append((8,5))
square_addresses.append(some_square)

#square 7
some_square = []
some_square.append((0,6))
some_square.append((0,7))
some_square.append((0,8))

some_square.append((1,6))
some_square.append((1,7))
some_square.append((1,8))

some_square.append((2,6))
some_square.append((2,7))
some_square.append((2,8))
square_addresses.append(some_square)

#square 8
some_square = []
some_square.append((3,6))
some_square.append((3,7))
some_square.append((3,8))

some_square.append((4,6))
some_square.append((4,7))
some_square.append((4,8))

some_square.append((5,6))
some_square.append((5,7))
some_square.append((5,8))
square_addresses.append(some_square)

#square 9
some_square = []
some_square.append((6,6))
some_square.append((6,7))
some_square.append((6,8))

some_square.append((7,6))
some_square.append((7,7))
some_square.append((7,8))

some_square.append((8,6))
some_square.append((8,7))
some_square.append((8,8))
square_addresses.append(some_square)

def address_to_box(address,array_board):
    return array_board[address[0]][address[1]]
def addresses_to_container(addresses,array_board):
    box_list = list(map(address_to_box,addresses,[array_board]*9))
    new_container = Container(box_list)
    for box in box_list:
        box.add_container(new_container)
    return new_container

all_addresses = row_addresses + column_addresses + square_addresses

def set_up_array_board(array_board):
    for address_set in all_addresses:
        addresses_to_container(address_set,array_board)
