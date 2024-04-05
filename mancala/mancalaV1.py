# MANCALA
import time
empty = " 04 " 
free = False


def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board,totalA,totalB,turn):
    count = 6
    print("                               ")
    print("----------------------")
    print("                               ")
    print("   Player {} board: ".format(turn))
    print("   +=============+")
    print("   |     " + totalB + "     |")
    print("   +=============+")
    for row in board:
        grid = (" | ").join(row)
        print(" "+str(count)+ (" | ") + grid + (" | "))
        count -= 1
    print("   +=============+")
    print("   |     " + totalA + "     |")
    print("   +=============+")
    print("                               ")
    print("----------------------")
    print("                               ")



def flipBoard(board):
  y = len(board) - 1
  for x in range(len(board)):
    board[x][1],board[y][0] = board[y][0], board[x][1]
    y -= 1
  return board

def formatScore(num):
    num = str(num)
    if len(num) > 1:
        return  num[0]+ " " + num[1]
    elif len(num) == 1:
        return   "0 " + num[0]

def formatSquare(num):
    num = str(num)
    if len(num) > 1:
        return  " " + num[0]+ num[1] + " "
    elif len(num) == 1:
        return   " 0" + num[0] + " "

def traverse(board,num,totalA,totalB,turn):
    global free
    count = 0 
    temp =  int(board[num][0] )
    start = num 
    side = 0
    board[start][side] = formatSquare(0)
    index  = start + 1 
    while count < temp:
        if count < temp and index <= len(board)  - 1 and side == 0:
            board[index][side]  = formatSquare(int(board[index][side]) + 1)
            index += 1
            count += 1
        elif count < temp and (index == len(board) or index == -1):
            if side == 0:
                totalA += 1
                if count == temp - 1 and turn == "A":
                  free = True
                  board, totalA,totalB = aTurn(board, totalA, totalB, turn)
                elif count == temp - 1 and turn == "B":
                  free = True
                  board, totalA,totalB = bTurn(board, totalA, totalB, turn)
                else:
                  side = 1
                  index = len(board) -1
            elif side == 1:
                totalB +=1
                side = 0
                index = 0
            count += 1
        elif count < temp and index >= 0 and side == 1:
          board[index][side]  =  formatSquare(int(board[index][side]) + 1)
          index -= 1
          count += 1
    
    board,totalA,totalB = capture(board,totalA,totalB,turn,index,side,count,temp)
    return board,totalA,totalB



def main(board,totalA,totalB):
  global free
  empty = False
  while empty == False:
    board, totalA,totalB = aTurn(board, totalA, totalB, "A")
    free = False
    displayBoard(board,formatScore(totalA),formatScore(totalB), "A")
    empty = checkEmpty(board)
    if empty == True:
      turn = "A"
      break
    time.sleep(1)
    board, totalB,totalA = bTurn(flipBoard(board), totalB, totalA, "B")
    free = False
    displayBoard(board,formatScore(totalA),formatScore(totalB), "B")
    empty = checkEmpty(board)
    turn = "B"
    flipBoard(board)
    time.sleep(1)
  endGame(board,totalA,totalB,turn)


def aTurn(board, totalA, totalB, turn):
  global free
  displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  inpA = len(board) - int(input(" Player A, please enter which slot to choose from: "))
  board, totalA,totalB = traverse(board,inpA,totalA,totalB,turn)
  if free == False:
    displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  return board, totalA,totalB

def bTurn(board, totalB, totalA, turn):
  global free
  displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  inpB = len(board) - int(input(" Player B, please enter which slot to choose from: ")) 
  board, totalB, totalA = traverse(board,inpB,totalB,totalA,turn)
  if free == False:
    displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  return board, totalB,totalA

def capture(board,totalA,totalB,turn,index,side,count,temp):
  print(count,temp)
  if count == tempand board[index][side] == " 00 ":
    if turn == "A" and side == 0:
      totalA += int(board[index][side + 1]) + 1
      board[index][side + 1] = " 00 "
      board[index][side] = " 00 "
    elif turn == "A" and side == 1:
      totalA += int(board[index][side - 1]) + 1
      board[index][side - 1] = " 00 "
      board[index][side] = " 00 "
    elif turn == "B" and side == 0:
      totalB += int(board[index][side - 1]) + 1
      board[index][side + 1] = " 00 "
      board[index][side] = " 00 "
    elif turn == "A" and side == 1:
      totalB += int(board[index][side - 1]) + 1
      board[index][side - 1] = " 00 "
      board[index][side] = " 00 "
  return board,totalA,totalB

def checkEmpty(board):
  for i in range(len(board)):
    if board[i][0] != " 00 ":
      return False
  return True

def endGame(board,totalA,totalB,turn):
  if turn == "A":
    totalA += 1
    for i in range(len(board)):
      boardB += int(board[i][1])
  elif turn == "B":
    totalB += 1
    for i in range(len(board)):
      boardA += int(board[i][1])
  winCheck(totalA,totalB)

def winCheck(totalA, totalB):
  if totalA > totalB:
    print("Player A won")
  elif totalB > totalA:
    print("Player B won")
  else:
    print("DRAW!!!")
  





board = makeBoard(2,6)
totalA = 0
totalB = 0
main(board,totalA,totalB)


