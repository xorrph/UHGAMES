# MANCALA
import time
empty = " 04 " 


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
  count = 0
  temp =  int(board[num][0] )
  board[num][0] = formatSquare(0)
  boardA,boardB = twoLists(board)
  f = False
  while count < temp:
    for a in range(num+1, len(boardA)):
      board,totalA,totalB,c = capture(oneList(boardA, boardB),totalA,totalB,turn,a,count,temp)
      boardA,boardB = twoLists(board)
      if c == False:
        boardA[a] = formatSquare(int(boardA[a]) + 1)
      count +=1
      if count >= temp:
          break
    totalA += 1
    count +=1
    if count >=temp:
        f = True
        break
    for b in range(len(boardB)-1,-1,-1):
      boardB[b] = formatSquare(int(boardB[b]) + 1)
      count +=1
      if count >= temp:
        break
  return oneList(boardA, boardB),totalA,totalB,f,c
    

def main(board,totalA,totalB):
  empty = False
  while empty == False:
    f = True
    turn = "A"
    while  f == True:
      board, totalA,totalB,f,c = aTurn(board, totalA, totalB, "A")# another while loop, while F ( Free turn) is true it repeats aTurn  , also if capture is true then break
      empty = checkEmpty(board)
      if empty == True:
        turn = "A"
        break
      if c == True:
        break
    time.sleep(1)
    f = True
    turn = "B"
    flipBoard(board)
    while  f == True:
      board, totalB,totalA,f,c= bTurn(board, totalB, totalA, "B")
      empty = checkEmpty(board)
      if empty == True:
        turn = "B"
        break
      if c == True:
        break
    flipBoard(board)
    time.sleep(1)
  endGame(board,totalA,totalB,turn)

def aTurn(board, totalA, totalB, turn):
  displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  inpA = len(board) - int(input(" Player A, please enter which slot to choose from: "))
  board, totalA,totalB,f,c = traverse(board,inpA,totalA,totalB,turn)# f is also returned
  displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  return board, totalA,totalB,f,c # f is also returned

def bTurn(board, totalB, totalA, turn):
  displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  inpB = len(board) - int(input(" Player B, please enter which slot to choose from: ")) 
  board, totalB, totalA,f,c = traverse(board,inpB,totalB,totalA,turn)
  displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  return board, totalB,totalA,f,c

def capture(board,totalA,totalB,turn,i,count,temp): 
  print("same",count , temp ,"00", board[i][0] )
  c = False
  if count == temp - 1 and board[i][0] == " 00 ":
    c = True
    print(c)
    totalA += int(board[i][1])  + 1
    board[i][1] = " 00 "
    board[i][0] = " 00 "
  return board,totalA,totalB,c
  

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
  
def twoLists(board):
  boardA = []
  boardB = []
  for i in range(len(board)):
    boardA.append(board[i][0])
    boardB.append(board[i][1])
  return boardA, boardB

def oneList(boardA,boardB):
  board = []
  for i in range(len(boardA)):
    board.append([boardA[i],boardB[i]])
  return board



boardA = []
boardB = []
board = makeBoard(2,6)
totalA = 0
totalB = 0
main(board,totalA,totalB)


