# MANCALA
empty = " 04 " 



def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board,totalA,totalB,turn):
    count = 6
    print("   Player {} board: ".format(turn))
    print("  +=============+")
    print("  |     " + totalB + "     |")
    print("  +=============+")
    for row in board:
        grid = (" | ").join(row)
        print(str(count )+ (" | ") + grid + (" | "))
        count -= 1
    print("  +=============+")
    print("  |     " + totalA + "     |")
    print("  +=============+")
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
    start = num 
    side = 0
    board[start][side] = formatSquare(0)
    index  = start + 1 
    while count < temp:
        if count < temp and index <=  len(board)  - 1 and side == 0:
            board[index][side]  = formatSquare(int(board[index][side]) + 1)
            index += 1
            count += 1
        elif count < temp and index == len(board) :
            if side == 0:
                totalA += 1
                side += 1
                index = len(board) -1
                if count == temp - 1 and turn == "A":
                  board = aTurn(board, totalA, totalB, turn)
                  break
                elif count == temp - 1 and turn == "B":
                  board = bTurn(board, totalB, totalA, turn)
                  break
            elif side == 1:
                totalB +=1
                side -= 1
                index = 0
            count += 1
        elif count < temp and index >= 0 and side == 1:
          board[index][side]  =  formatSquare(int(board[index][side]) + 1)
          index -= 1
          count += 1
    return board, totalA,totalB



def main(board,totalA,totalB):
  board = aTurn(board, totalA, totalB, "A")
  board = bTurn(flipBoard(board), totalB, totalA, "B")



def aTurn(board, totalA, totalB, turn):
  displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  inpA = len(board) - int(input("Please enter which number to choose from: ")) 
  board, totalA,totalB = traverse(board,inpA,totalA,totalB,turn)
  print("second display")
  displayBoard(board,formatScore(totalA),formatScore(totalB), turn)
  return board

def bTurn(board, totalB, totalA, turn):
  displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  inpB = len(board) - int(input("Please enter which number to choose from: ")) 
  board, totalB, totalA = traverse(board,inpB,totalB,totalA,turn)
  displayBoard(board,formatScore(totalB),formatScore(totalA), turn)
  return board
  
  
#to-do:
#display board include playerA or playerB
#add turnFlag (0 = A 1 = B)
#free turn and capture
#check for empty board
#collect total from the players designated side

    


board = makeBoard(2,6)
totalA = 0
totalB = 0
main(board,totalA,totalB)
x = input("test")


