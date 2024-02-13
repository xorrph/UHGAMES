#wordle
empty = " "
import random
import time

def makeBoard(width,length):
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board):
  for row in board:
    grid = (" | ").join(row)
    print(" -------------------------")
    print((" | ") + grid + (" | "))
  print(" -------------------------")


def randomWord():
    file = open("answer.txt", "r")
    content = file.readlines()
    x = random.randint(0,len(content))
    word = content[x]
    return word

def validWord(userInput):
  f = open("wordle.txt", "r")
  content = f.readlines()
  while  True:
    userInput  = " " + userInput + " "
    for x in content:
     f.flush()
     if x.find(userInput) != -1:
       print("Valid")
       return userInput.strip( )
        
    userInput = input("Enter a 6 letter word:  ").lower()
    


def checkAnswer(userInput, answer):
    clue = []
    for index in range(len(userInput)):
      if index == answer.find(userInput[index] ):
        clue.append("+")
      elif answer.find(userInput[index]) != -1:
        clue.append("-")
      else:
        clue.append("x")
    return clue


def changeBoard(board, clue, guess):
  for letter in range(6):
    board[guess][letter] = clue[letter]
  guess += 1
  return guess, board
  

guess = 0
board =makeBoard(6,6)
displayBoard(board)
word = randomWord()
print(word)
userInput = input("Enter a 6 letter word:  ").lower()
userInput = validWord(userInput)
clue = checkAnswer (userInput, word)
guess, board = changeBoard(board, clue, guess)
displayBoard(board)
input()
