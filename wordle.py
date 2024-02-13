#wordle
empty = " "
import random

def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board):
  for row in board:
    grid = (" | ").join(row)
    print(" ---------------------")
    print((" | ") + grid + (" | "))
  print(" ---------------------")

    


def randomWord(content):
    x = random.randint(0,len(content))
    y = random.randint(0,len(content[x]))
    word = content[x][y]
    return word

def validWord(userInput):
    return userInput



def checkAnswer(userInput, answer):
    return userInput

f = open("wordle.txt", "r")
content = f.readlines()


board =makeBoard(5,6)
displayBoard(board)
word = randomWord(content)
print(word)


input()
