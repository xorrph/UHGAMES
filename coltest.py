import time

width = 5
length = 5
empty = ' - '

def makeBoard(width, length):
    global empty 
    board = []
    for i in range(length):
        board.append([empty] * width)
    return board 

def displayBoard(board):
    for row in board:
        grid = (" | ").join(row)
        print((" | ") + grid + (" | "), end='\n')  # Use \n to move to the next line

def overwriteLine():
    print("\033[F\033[K", end='')  # Move the cursor up one line and clear the line


print("This is line can not be removed")


board = makeBoard(width, length)
displayBoard(board)
time.sleep(1)

board[0][0] = " # "
overwriteLine()
displayBoard(board)
time.sleep(1)

board[0][1] = " # "
overwriteLine()
displayBoard(board)
time.sleep(1)

board[0][2] = " # "
overwriteLine()
displayBoard(board)
time.sleep(1)

board[0][3] = " # "
overwriteLine()
displayBoard(board)
time.sleep(1)

x = input("test")
