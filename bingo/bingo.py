empty = " -- "
import time

def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displaySingleBoard(board,width,user):
    print("{}'s board: ".format(user))
    for row in board:
        grid = (" | ").join(row)
        print(" +" + ("------+" * width))
        print((" | ") + grid + (" | "))
    print(" +" + ("------+" * width))

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
    for c in range(turns):
                user =input("Player {}, please enter your name: ".format(c + 1))
                board = makeBoard(width,length)
                boards.append(board)
                players.append(user)
                displaySingleBoard(board,width,user)
    enter(boards,players,length,width)
    displayAllBoards(boards,players,length,"","")
    r = 1
    while end == False:
      print("")
      print(" Round {}".format(r))
      changes, bingos, boards, num =  randomNum(bingos,boards,players,length,width)
      topline = displayRandomNum( num, players,width)
      L = dispChange(changes,width)
      displayAllBoards(boards,players,width,topline,L)
      time.sleep(2.5)
      r += 1
      end = endGame(boards,players,length,width) # do this + add comments to this and mancala

def enter(boards,players,length,width):
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        inp = input("{}, please enter a number between 1 and 99: ".format(players[c]))
        inp = checkInp(inp,boards, players,c)
        boards[c][row][index] = " " + '{:0>2}'.format(int(inp)) + " "
        displaySingleBoard(boards[c],length,players[c])

def displayRandomNum(num, players,width):
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

def dispChange(changes,length):
  L = " "
  for i in range(len(changes)):
    if changes[i]== 1:
      L += ("x" * 7) * length + "x "
    else:
      L +=("-" * 7) * length + "- "
    if i < len(changes) -1:
      L +="      "
  return L
    
  
  
  
 
def displayAllBoards(boards,players,width,topline,L):
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


def randomNum(bingos,boards,players,length,width):
  import random
  changes= []
  flag = False
  cF = False
  while flag == False:
    r = random.randint(1,99)
    rFormat = " " + '{:0>2}'.format(int(r)) + " "
    if rFormat not in bingos:
      flag = True
      bingos.append(rFormat)
      for c in range(len(players)):
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



def endGame(boards,players,length,width):
  for c in range(len(players)):
    for row in range(length):
      for index in range(width):
        if boards[c][row][index] != " XX ":
          return False
    print("Player {} won!!".format(players[c]))
    return True


# to do
# fix endGame function
# add comments
        

start()
input()
