

width = 7
length = 6

def displayBanner():
  print("=============")
  print("=                              =")
  print("=    CONNECT 4     =")
  print("=                              =")
  print("=============")
  print("")


def makeBoard(width,length):
    global empty 
    board = []
    for i in range(length):
       board.append([empty] * width)
    return board 

def displayBoard(board):
    temp = 0
    for x in board:
           grid = (" ".join(x))
           print(grid)
           

def add(board,slot,char):
  global empty 
  for i in range(9, -1, -1):
    if board[i][slot] == empty:
      board[i][slot] = char
      return board
  print("Slot is full")
  return board
  

def charCheck(char1):
    global empty 
    while True:
      if char1.lower()  == "d" :
        x = b'\xb1'.decode('cp437')
        char1 = " " + x + " "
        x = b'\xb2'.decode('cp437')
        char2 = " " + x + " "
        return char1,char2
      elif char1.lower == "h" :
        char1 = " ♥ "
        char2 =" ♦"
        return char1,char2
      else:
             char1= input("Please enter if you want to be lighter or darker:  ")

def main(board,user1,user2,char1,char2):
    win = False
    full = False
    while win != True and full != True:
        slot1 = int(input("{}, please enter which slot do you want to put your character in: ".format(user1))) - 1
        board = add(board,slot1,char1)
        displayBoard(board)
        full = isFull(board)
        slot2 = int(input("{}, please enter which slot do you want to put your character in: ".format(user2))) - 1
        board = add(board,slot2,char2)
        displayBoard(board)
        full = isFull(board)
        

def isFull(board):
    global empty
    for i in range(10):
        if board[0][i] == empty:
          return False
    return True
        
displayBanner()
empty  = ' - '
user1 = input("Please enter your name: ")
char1= input("Please enter if you want to be lighter or darker:  ")
char1,char2 = charCheck(char1)
user2 = input("Please enter your name: ")
board = makeBoard(width,length)
displayBoard(board)
main(board,user1,user2,char1,char2)\

# ~
# o
# =

