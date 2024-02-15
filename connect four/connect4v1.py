# global variables and inbuilt python imports
empty = " - "
turn = 0
length = 0
import os
import time

def displayBanner(): #overwrite each print statement showing the word four get connected
    print("""
===================================
=                                 =
=          CONNECT FOUR           =
=                                 =
===================================
""", end="\r", flush=True)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
    print("""
===================================
=                                 =
=          CONNECT #OUR           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
    print("""
===================================
=                                 =
=          CONNECT ##UR           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
    print("""
===================================
=                                 =
=          CONNECT ###R           =
=                                 =
===================================
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
    print("""
===================================
=                                 =
=          CONNECT ####           =
=                                 =
===================================
""")


def makeBoard(width,length): #create the board using python lists
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board):#print the board by joining the items within the list with a |
  for row in board:
    grid = (" | ").join(row)
    print((" | ") + grid + (" | "))


def checkSize(length,width):#make sure the size allows for the connect four
    if length < 4 or width < 4:
        length = int(input("Enter the length of the board: "))
        width = int(input("Enter the width of the board: "))
        

def add(board,slot,char):#adds the players character into a slot
  global empty 
  global length
  for i in range(length-1, -1, -1):
    if board[i][slot] == empty:
      board[i][slot] = char
      return i, board
  print("Slot is full")
  return 0, board


def charCheck(char, other, name):# check if the characters are valid and are not the same as in-built characters 
    while True:
      if len(char) != 1 or char == '-' or char == "#" or char == other:
        char = input(name + ", invalid character, please try again: ")
      else:
             char = " " + char + " "
             return char
        

def main(board,user1,user2,char1,char2): # main gameplay loop
    # initialise variables
    global turn # even or odd decides which players turn it is
    win = False
    full = False
    turn = -1
    # keep running the code as long as someone has not won and the board is not full ( usually acts as a condition check for player 2)
    while win != True and full != True:
        #player 1
        turn += 1
        slot1 = int(input("{}, please enter which slot do you want to put your character in: ".format(user1))) - 1 # take into account user does not read board like 0, 1 ,2 to access that position so we add one
        pos, board = add(board,slot1,char1)# call add function and assign the returned values to the two values
        displayBoard(board)#call the display board function to show the user the new changes
        win = checkWin(board,char1,slot1,pos) # check for a win
        full = isFull(board)# check if its full
        if win == True or full == True: # do the while loop condition in the middle to check for player 1
          break
        #player 2 
        turn += 1
        slot2 = int(input("{}, please enter which slot do you want to put your character in: ".format(user2))) - 1
        pos, board = add(board,slot2,char2)
        displayBoard(board)
        win = checkWin(board,char2,slot2,pos)
        full = isFull(board)
    return win, full

def winHorz(board,char,slot,pos): # check if there is a horizontal win
  four = []
  count = 0
  temp = slot
  for i in range(len(board)-slot):#checks right
    if board[pos][temp] == char and temp >= 0:
      count += 1
      four.append([pos,temp])
      temp += 1
    else:
      break
  temp = slot - 1
  for i in range(slot):# checks left
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
  for i in range(len(board)-pos):#checks up
    if board[temp][slot] == char and temp >= 0:
      count += 1
      four.append([temp,slot])
      temp += 1
    else:
      break
  temp = pos - 1
  for i in range(pos):# checks down
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

def winDiagRL(board,char,slot,pos): # check if there is a diagonal win (this diagonal goes from the right side of the board to the left)
  four = []
  count = 0
  print(pos,slot)
  tempPos = pos
  tempSlot = slot
  while tempPos <= len(board)-1 and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0: #checks up the diagonal
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
  while tempPos <= len(board)-1and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:#checks down the diagonal
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

def winDiagLR(board,char,slot,pos): # check if there is a diagonal win(this diagonal goes from the left  side of the board to the right)
  four = []
  count = 0
  tempPos = pos
  tempSlot = slot
  while tempPos <= len(board)-1 and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:#checks up the diagonal
    if board[tempPos][tempSlot] == char:
      count += 1
      four.append([tempPos,tempSlot])
      tempPos += 1
      tempSlot -= 1
    else:
      break
  tempPos = pos -1
  tempSlot = slot
  while tempPos <= len(board)-1and tempSlot <= len(board)-1 and tempPos >= 0 and tempSlot >= 0:#checks down the diagonal
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
  
def checkWin(board,char,slot,pos): # check if there is a win via all the win functions
  four = []
  #each function returns a list of the positions of the winning characters, so as long as the list is of size 4 that means 4 have been connected and hence a win
  if len(winHorz(board,char,slot,pos)) == 4:
    four = winHorz(board,char,slot,pos)
  elif len(winVert(board,char,slot,pos)) == 4:
    four = winVert(board,char,slot,pos)
  elif len(winDiagRL(board,char,slot,pos)) == 4:
    four = winDiagRL(board,char,slot,pos)
  elif len(winDiagLR(board,char,slot,pos)) == 4:
    four = winDiagLR(board,char,slot,pos)

  if four != []: # the win functions return an empty list if it does not reach a connect 4 so this only shows the win board if theres a win 
    showWin(board,four)
    return True
  else:
    return False
  
    
    
def showWin(board,four): # show the winning character positions
  for pos in four:
    board[pos[0]][pos[1]] = ' # '


def isFull(board): # checks if the board is full
    global empty
    global length
    #iterates through the top row and checks each row to see if it is empty
    for i in range(length):
        if board[0][i] == empty:
          return False
    return True

def start(): # initialise game and variables and user inputs
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

def endWin(user1,user2,char1,char2,win,full,board): #ends the game or repeats it
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

