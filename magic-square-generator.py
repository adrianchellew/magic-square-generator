"""
A magic square generator that allows the user to enter
the N size of a magic square as any positive odd integer.
The program then calculates, prints and verifies the magic square.
"""

from math import floor

# Function that creates and calculates a valid magic square.
def create_magic_sq(size):
    magic_sq = [[0]*size for i in range(size)]

    row = 0
    col = floor(size/2)

    prev_row = row
    prev_col = col

    magic_sq[row][col] = 1

    current_num = 2

    while current_num <= size*size:

        if row-1 < 0:
            row = size-1
        else:
            row -= 1
           
        if col+1 == size:
            col = 0
        else:
            col += 1
           
        if magic_sq[row][col] == 0:
            magic_sq[row][col] = current_num
        else:
            row = prev_row
            col = prev_col
           
            if row+1 == size:
                row = 0
            else:
                row += 1
           
            magic_sq[row][col] = current_num
           
        prev_row = row
        prev_col = col
           
        current_num += 1

    return magic_sq

# Function that prints a magic square.
def print_magic_sq(magic_sq):
    for row in magic_sq:
        for val in row:
            print('{:4d}'.format(val), end='')
        print()

# Function that checks whether a magic square is valid.
def verify_magic_sq(magic_sq):
    size = len(magic_sq)
  
    sum_list = []

    # Calculate the rows
    for row in magic_sq:
        sum_list.append(sum(row))

    # Calculate the columns
    for col in range(size):
        sum_list.append(sum([row[col] for row in magic_sq]))

    # Calculate the first diagonal
    diag_1 = 0
    for i in range(size):
        diag_1 += magic_sq[i][i]
    sum_list.append(diag_1)

    # Calculate the second diagonal
    diag_2 = 0
    for x in range(size):
        diag_2 += magic_sq[x][(size-1)-x]
    sum_list.append(diag_2)
    
    return len(set(sum_list)) == 1

# Ask a user to input the size of the magic square
size = 0
while size < 1 or size%2 == 0:
    while True:
        try:
            size = int(input("Enter any positive odd number to generate a magic square: "))
            break
        except ValueError:
            print("Oops!  That wasn't a valid number.  Try again...")

# Create the magic square
magic_square = create_magic_sq(size)

# Print the magic square
print()
print('Printing magic square...')
print()
print_magic_sq(magic_square)
print()

# Verify the magic square
if verify_magic_sq(magic_square):
    print('Correct! A valid magic square!')
else:
    print('Incorrect! An invalid magic square.')