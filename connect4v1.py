
empty = " - "
turn = 0
length = 0
import os
import time

def displayBanner():
    print("""
===================================
=                                 =
=          CONNECT FOUR           =
=                                 =
===================================
""", end="\r", flush=True)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("""
===================================
=                                 =
=          CONNECT #OUR           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("""
===================================
=                                 =
=          CONNECT ##UR           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("""
===================================
=                                 =
=          CONNECT ###R           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("""
===================================
=                                 =
=          CONNECT ####           =
=                                 =
===================================
""")


def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board):
  for row in board:
    grid = (" | ").join(row)
    print((" | ") + grid + (" | "))


def checkSize(length,width):
    if length < 4 or width < 4:
        length = int(input("Enter the length of the board: "))
        width = int(input("Enter the width of the board: "))
        

def add(board,slot,char):
  global empty 
  global length
  for i in range(length-1, -1, -1):
    if board[i][slot] == empty:
      board[i][slot] = char
      return i, board
  print("Slot is full")
  return 0, board


def charCheck(char, other, name):# check if the characters are valid and assign the correct variables 
    while True:
      if len(char) != 1 or char == '-' or char == "#" or char == other:
        char = input(name + ", invalid character, please try again: ")
      else:
             char = " " + char + " "
             return char
        

def main(board,user1,user2,char1,char2): # main gameplay loop
    global turn
    win = False
    full = False
    turn = -1
    while win != True and full != True:
        turn += 1
        slot1 = int(input("{}, please enter which slot do you want to put your character in: ".format(user1))) - 1
        pos, board = add(board,slot1,char1)
        displayBoard(board)
        win = checkWin(board,char1,slot1,pos)
        full = isFull(board)
        if win == True or full == True:
          break
        turn += 1
        slot2 = int(input("{}, please enter which slot do you want to put your character in: ".format(user2))) - 1
        pos, board = add(board,slot2,char2)
        print(pos)
        displayBoard(board)
        win = checkWin(board,char2,slot2,pos)
        full = isFull(board)
    return win, full

def winHorz(board,char,slot,pos): # check if there is a horizontal win
  four = []
  count = 0
  temp = slot
  for i in range(len(board)-slot):
    if board[pos][temp] == char and temp >= 0:
      count += 1
      four.append([pos,temp])
      temp += 1
    else:
      break
  temp = slot - 1
  for i in range(slot):
    if board[pos][temp] == char and temp >= 0:
      count += 1
      four.append([pos,temp])
      temp -= 1
    else:
      break
  if count == 4:
    return four
  else:
    return []

def winVert(board,char,slot,pos): # check if there is a vertical win
  four = []
  count = 0
  temp = pos 
  for i in range(len(board)-pos):
    if board[temp][slot] == char and temp >= 0:
      count += 1
      four.append([temp,slot])
      temp += 1
    else:
      break
  temp = pos - 1
  for i in range(pos):
    if board[temp][slot] == char and temp >= 0:
      count += 1
      four.append([temp,slot])
      temp -= 1
    else:
      break
  if count == 4:
    return four
  else:
    return []

def winDiagRL(board,char,slot,pos): # check if there is a diagonal win
  four = []
  count = 0
  print(pos,slot)
  tempPos = pos
  tempSlot = slot
  while tempPos <= len(board)-1 and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:
    if board[tempPos][tempSlot] == char:
      print(tempPos,tempSlot)
      count += 1
      four.append([tempPos,tempSlot])
      tempPos += 1
      tempSlot += 1
    else:
      break
  tempPos = pos - 1 
  tempSlot = slot - 1
  while tempPos <= len(board)-1and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:
    print("test", tempPos,tempSlot)
    if board[tempPos][tempSlot] == char:
      count += 1
      four.append([tempPos,tempSlot])
      tempPos -= 1
      tempSlot -= 1
    else:
      break
  if count == 4:
    return four
  else:
    return []

def winDiagLR(board,char,slot,pos): # check if there is a diagonal win
  four = []
  count = 0
  tempPos = pos
  tempSlot = slot
  while tempPos <= len(board)-1 and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:
    if board[tempPos][tempSlot] == char:
      count += 1
      four.append([tempPos,tempSlot])
      tempPos += 1
      tempSlot -= 1
    else:
      break
  tempPos = pos -1
  tempSlot = slot
  while tempPos <= len(board)-1and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:
    if board[tempPos][tempSlot] == char:
      count += 1
      four.append([tempPos,tempSlot])
      tempPos -= 1
      tempSlot += 1
    else:
      break
  if count == 4:
    return four
  else:
    return []
  
def checkWin(board,char,slot,pos): # check if there is a win
  four = []
  if len(winHorz(board,char,slot,pos)) == 4:
    four = winHorz(board,char,slot,pos)
  elif len(winVert(board,char,slot,pos)) == 4:
    four = winVert(board,char,slot,pos)
  elif len(winDiagRL(board,char,slot,pos)) == 4:
    four = winDiagRL(board,char,slot,pos)
  elif len(winDiagLR(board,char,slot,pos)) == 4:
    four = winDiagLR(board,char,slot,pos)

  if four != []:
    showWin(board,four)
    return True
  else:
    return False
  
    
    
def showWin(board,four): # show the winning movements
  for pos in four:
    board[pos[0]][pos[1]] = ' # '


def isFull(board): # checks if the board is full
    global empty
    global length
    for i in range(length):
        if board[0][i] == empty:
          return False
    return True

def start(): # initialise game and variables
    global turn
    global length
    turn = 0
    length = int(input("Enter the length of the board: "))
    width = int(input("Enter the width of the board: "))
    checkSize(length,width)
    empty  = ' - '
    user1 = input("Player 1, please enter your name: ")
    char1= input("Please enter a character of your choosing:  ")
    char2 = ""
    char1 = charCheck(char1, char2, user1)
    user2 = input("Player 2, please enter your name: ")
    char2 = input("Please enter a character of your choosing: ")
    char2 = charCheck(char2, char1,user2)
    board = makeBoard(width,length)
    displayBoard(board)
    full, win = main(board,user1,user2,char1,char2)
    endWin(user1,user2,char1,char2,full,win,board)

def endWin(user1,user2,char1,char2,win,full,board):
    global turn
    if win == True:
        if turn % 2 == 0:
            print("{} wins using the {} character!".format(user1,char1.strip(" ")))
        else:
            print("{} wins using the {} character!".format(user2,char2.strip(" ")))
    elif full == True:
        print("Board is full! It's a tie!!")
    displayBoard(board)
    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain.upper() == "Y":
        start()
    else:
        print("Thanks for playing!!")
    



    
displayBanner()
start()




### (C) Naglis Slamiskis 04-02-24 14:51pm

