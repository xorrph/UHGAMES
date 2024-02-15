empty = " -- "
import time

def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displaySingleBoard(board,length,user):
    print("{}'s board: ".format(user))
    for row in board:
        grid = (" | ").join(row)
        print(" +" + ("------+" * length))
        print((" | ") + grid + (" | "))
    print(" +" + ("------+" * length))

def checkInp(inp,boards, players,c):
  while True:
    inp = " " + '{:0>2}'.format(int(inp)) + " "
    flag = False
    for row in boards[c]:
      for num in row:
        if inp == num:
          flag = True
      if flag == True:
        break
    if int(inp) >100 and int(inp) <= 1:
      flag = True
    if flag == False:
      return inp
    print("")
    print("INVALID")      
    inp = input("{}, please re-enter a number between 1 and 100: ".format(players[c]))
    print("")


def start(): # initialise game and variables
    boards = []
    players = []
    end = False
    turns = int(input("Enter how many players are playing: "))
    length = int(input("Enter the length of the board: "))
    width = int(input("Enter the width of the board: "))
    for c in range(turns):
                user =input("Player {}, please enter your name: ".format(c + 1))
                board = makeBoard(width,length)
                boards.append(board)
                players.append(user)
                displaySingleBoard(board,length,user)
    enter(boards,players,length,width)
    displayAllBoards(boards,players,length,"")
    r = 1
    while end == False:
      print("")
      print("Round {}".format(r))
      boards, num =  randomNum(boards,players,length,width)
      topline = displayRandomNum( num, players,length)
      displayAllBoards(boards,players,length,topline)
      time.sleep(1)
      r += 1
      end = endGame(boards,players,length,width) # do this + add comments to this and mancala

def enter(boards,players,length,width):
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        inp = input("{}, please enter a number between 1 and 100: ".format(players[c]))
        inp = checkInp(inp,boards, players,c)
        boards[c][row][index] = " " + '{:0>2}'.format(int(inp)) + " "
        displaySingleBoard(boards[c],length,players[c])

def displayRandomNum(num, players,length):
  line = "======="
  newLine = "="
  mid = ""
  for i in range(length):
    newLine += line
    mid += " "
  x = (" " + ((newLine )+ "=======") * (len(players) -1 ) + newLine)
  print(x)
  print(" " + "<" * (int((len(x) - 24)/2)) +" The Bingo Number is" + num + ">" * (int((len(x) - 24)/2) -1) )
  return x


 
def displayAllBoards(boards,players,length,topline):
  print(topline)
  lines2 = ""
  for j in range(len(boards[0])):
    lines1 = ""
    nums = ""
    for index in range(len(boards)):
      grid = (" | ").join(boards[index][j])
      lines1 = (lines1 + " +" + ("------+" * length) + "      ")
      nums = (nums + (" | ") + grid + (" | ") + "     ")
    print(lines1)
    print(nums)
  print(lines1)
  return lines1


def randomNum(boards,players,length,width):
  import random
  r = random.randint(1,100)
  rFormat = " " + '{:0>2}'.format(int(r)) + " "
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        if boards[c][row][index] == rFormat:
          boards[c][row][index] = " XX "
  return boards, rFormat



def endGame(boards,players,length,width):
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        if boards[c][row][index] != " XX ":
          return False
    return True



        

start()
input()
