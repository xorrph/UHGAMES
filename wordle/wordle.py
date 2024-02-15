#wordle
#global variables and imports
empty = " "
import random

def makeBoard(width,length): # make the board (this is a static 6  by 6 since words are 6 long and there are 6 guesses)
  global empty 
  board = []
  for i in range(length):
     board.append([empty] * width)
  return board 

def displayBoard(board): # display the board and guesses made
  for row in board:
    grid = (" | ").join(row)
    print(" -------------------------")
    print((" | ") + grid + (" | "))
  print(" -------------------------")


def randomWord(): # select a random word from a text file containing common 6 letter words
    file = open("answer.txt", "r")
    content = file.readlines() 
    x = random.randint(0,len(content))# select a random word
    word = content[x]
    return word

def validWord(userInput): # check if the word inputted by the user is a valid word, checked against a larger text file containing alot more words
  f = open("wordle.txt", "r")
  content = f.readlines()
  while  True:
    userInput  = " " + userInput + " "
    for x in content:
     f.flush()
     if x.find(userInput) != -1:
       return userInput.strip( )
        
    userInput = input(" Invalid word, enter a 6 letter word: ").lower()
    


def checkAnswer(userInput, answer):
    clue =["","","","","",""] # initialise the clue variable
    for index in range(len(userInput)):
        try: # .index() returns an error so we catch the error and add an x to show that the letter has not been found
          if index == answer.index(userInput[index] ):#check if the letter is in the same place
            answer[index] = ("!")# this accounts for duplicate letters making sure the clues given are accurate
            clue[index] = ("+")#correct place
          elif userInput[index] in answer:
                answer[answer.index(userInput[index])] = ("!")# this accounts for duplicate letters making sure the clues given are accurate
                clue[index] = ("-")#in the word not correct place
        except:
             clue[index] = ("x")# not in the word
    return clue


def changeBoard(board, clue, guess):
  for letter in range(6): # add the new word
    board[guess][letter] = clue[letter]
  return board

def checkWin(guess,board):#check if the word has been guessed
  for index in range(len(board)):
    if board[guess ][index] != "+": # if it finds anything other than a correct letter it returns false
      return False
  return True #all values were correct thus returns true

def end(win,answer,guess): #end of game
  if win == True:
    print(" Congratulations, you won in {} tries".format(guess)) 
  else:
    print(" You lost, the word was {}, better luck next time!".format(answer.strip()))

#todo
#make the game loop if the player wants to continue playing

guess = 0
board =makeBoard(6,6)
displayBoard(board)
word = randomWord()
win = False
while guess < 6:
  userInput = input(" Enter a 6 letter word: ").lower()
  userInput = validWord(userInput)
  clue = checkAnswer (userInput, list(word))
  board = changeBoard(board, clue, guess)
  if  checkWin(guess ,board) == True:
    win = True
    guess += 1
    displayBoard(board)
    break
  guess += 1
  displayBoard(board)
end(win,word,guess)
input()
