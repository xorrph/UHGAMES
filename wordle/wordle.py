#wordle
#global variables and imports
import random

def makeBoard(width,length): # make the board (this is a static 6  by 6 since words are 6 long and there are 6 guesses)
  empty = " "
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
    x = random.randint(0,len(content) - 1)# select a random word
    word = content[x]
    return word

def validWord(userInput): # check if the word inputted by the user is a valid word, checked against a larger text file containing alot more words
  f = open("wordle.txt", "r")
  content = f.readlines()
  while  True:
    userInput  = " " + userInput + " "
    for x in content:
     if x.find(userInput) != -1:
       return userInput.strip( )
        
    userInput = input(" Invalid word, enter a 6 letter word: ").lower()
    


def checkAnswer(userInput, answer):
    clue =["","","","","",""] # initialise the clue variable
    for index in range(len(userInput)):
        if userInput[index] == answer[index]:#check if the letter is in the same place
          answer[index] = ("@")# this accounts for duplicate letters making sure the clues given are accurate
          clue[index] = ('+')#correct place
    for index in range(len(userInput)):
          if userInput[index] in answer and answer[index] != "@":
              answer[answer.index(userInput[index])] = ("!")# this accounts for duplicate letters making sure the clues given are accurate
              clue[index] = ("?")#in the word not correct place
          elif userInput[index] not in answer and answer[index] != "@":
              clue[index] = ("X")
    return clue


def changeBoard(board, clue, guess):
  for letter in range(6): # add the new word to the board
    board[guess][letter] = clue[letter]
  return board

def checkWin(clue):#check if the word has been guessed
  if clue == ['+']*6:# check if the users word is equal to the answer
    return True# if so return True
  else:
    return False# else return False

def end(win,answer,guess): #end of game
  if win == True:
    print(" Congratulations, you won in {} tries".format(guess)) 
  else:
    print(" You lost, the word was {}, better luck next time!".format(answer.strip()))
  yn = input(" Do you want to play again (Y/N)? ")
  if yn.upper() == "Y":
    main()
  else:
    input(" Thanks for playing!")


def main():
  guess = 0
  board =makeBoard(6,6)
  displayBoard(board)
  word = randomWord()
  win = False
  while guess < 6: #only give 6 guesses
    userInput = input(" Enter a 6 letter word: ").lower()#make sure its always lowercase
    userInput = validWord(userInput)
    clue = checkAnswer (userInput, list(word))
    board = changeBoard(board, clue, guess)
    if checkWin(clue) == True: # check the condition the win condition after a turn
      win = True
      guess += 1
      displayBoard(board)
      break
    guess += 1
    displayBoard(board)
  end(win,word,guess)


main()
