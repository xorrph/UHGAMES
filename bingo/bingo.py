empty = " -- "
import time

def makeBoard(width,length): # initialise board
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displaySingleBoard(board,width,user): # print the board for one player
    print("{}'s board: ".format(user))
    for row in board:
        grid = (" | ").join(row)
        print(" +" + ("------+" * width))
        print((" | ") + grid + (" | "))
    print(" +" + ("------+" * width))

def checkInp(inp,boards, players,c): #check if the input is between 1 and 99 and also if it is not repeated in the players board already
  while True:
    inp = " " + '{:0>2}'.format(int(inp)) + " "
    flag = False
    for row in boards[c]: # this loop checks for reptition 
      for num in row:
        if inp == num:
          flag = True
      if flag == True:
        break
    if int(inp) >100 or int(inp) < 1: #this checks if it is wthin the boundaries of 1 to 99
      flag = True
    if flag == False:
      return inp
    print("")
    print("INVALID")      
    inp = input("{}, please re-enter a number between 1 and 99: ".format(players[c]))
    print("")


def start(): # initialise game and variables
    boards = []
    players = []
    bingos = []
    end = False
    turns = int(input("Enter how many players are playing: "))
    length = int(input("Enter the length of the board: "))
    width = int(input("Enter the width of the board: "))
    for c in range(turns): # allows each player to enter their username / name and a number into their board
                user =input("Player {}, please enter your name: ".format(c + 1))
                board = makeBoard(width,length) 
                boards.append(board)
                players.append(user)
                displaySingleBoard(board,width,user)
    enter(boards,players,length,width)
    displayAllBoards(boards,players,width,"","")
    r = 1
    while end == False: # loops through until someone has a bingo board
      print("")
      print(" Round {}".format(r))
      changes, bingos, boards, num =  randomNum(bingos,boards,players,length,width)
      topline = displayRandomNum( num, players,width)
      L = dispChange(changes,width)
      displayAllBoards(boards,players,width,topline,L)
      time.sleep(2.5)
      r += 1
      end = endGame(boards,players,length,width) # checks if someone has a fully crossed out board

def enter(boards,players,length,width): # lets the player enter a number for their board
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        inp = input("{}, please enter a number between 1 and 99: ".format(players[c]))
        inp = checkInp(inp,boards, players,c)
        boards[c][row][index] = " " + '{:0>2}'.format(int(inp)) + " "
        displaySingleBoard(boards[c],width,players[c])

def displayRandomNum(num, players,width): # displays the random bingo number
  line = "======="
  newLine = "="
  mid = ""
  for i in range(width):
    newLine += line
    mid += " "
  x = (" " + ((newLine )+ "=======") * (len(players) -1 ) + newLine)
  print(x)
  print(" " + "<" * (int((len(x) - 24)/2)) +" The Bingo Number is" + num + ">" * (int((len(x) - 24)/2) -1) )
  return x

def dispChange(changes,length): # change the displayAllBoards formatting if a board gets a number crossed of
  L = " "
  for i in range(len(changes)):
    if changes[i]== 1:
      L += ("x" * 7) * length + "x "
    else:
      L +=("-" * 7) * length + "- "
    if i < len(changes) -1:
      L +="      "
  return L
    
  
  
  
 
def displayAllBoards(boards,players,width,topline,L): # displays each board on the same line
  print(topline)
  print("")
  print(L)
  lines2 = ""
  for j in range(len(boards[0])):
    lines1 = ""
    nums = ""
    for index in range(len(boards)):
      grid = (" | ").join(boards[index][j])
      lines1 = (lines1 + " +" + ("------+" * width) + "      ")
      nums = (nums + (" | ") + grid + (" | ") + "     ")
    print(lines1)
    print(nums)
  print(lines1)
  print(L)
  print("")
  print(topline)
  return lines1


def randomNum(bingos,boards,players,length,width): # generates a random number and checks on each board if it is  on the board then crosses it out
  import random
  changes= []
  flag = False
  cF = False
  while flag == False:
    r = random.randint(1,99) # generates random number
    rFormat = " " + '{:0>2}'.format(int(r)) + " " # formats the number to be of format 00
    if rFormat not in bingos: # code to not repeat numbers
      flag = True
      bingos.append(rFormat)
      for c in range(len(players)): # checks if nunber is on a board then crosses it out
        for row in range(length):
          for index in range(width):
            if boards[c][row][index] == rFormat:
              boards[c][row][index] = " XX "
              cF = True
              break
        if cF == True: 
          changes.append(1)
          cF = False
        else:
          changes.append(0)
            
  return changes, bingos, boards, rFormat



def endGame(boards,players,length,width): # checks for a full board
  wins = []
  for p in players: # intialises the list to check if there is a win
    wins.append(True)
  for c in range(len(players) ):
    for row in range(length):
      for index in range(width):
        if boards[c][row][index] != " XX ": # if it finds a value that is not crossed out then it sets the board to false and exits out of looping through the board
          wins[c]= False
          break
  for w in range(len(wins)): #loops to check if anyone has a win board in the list
    if wins[w] == True:
      print("{} won!!".format(players[w]))
      return True
  return False


        

start()
input()
