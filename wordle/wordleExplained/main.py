
#main
#controls the flow of the game and initalises everything


def main():
  guess = 0# initalise guess to be 0
  board =makeBoard(6,6)# initalise the board
  displayBoard(board)#display the empty board
  word = randomWord()#choose a random word as the answer
  win = False# set win to be false
  while guess < 6: #only give 6 guesses
    userInput = input(" Enter a 6 letter word: ").lower()#ask the user to enter a word make sure its always lowercase
    userInput = validWord(userInput)# get the user to enter a valid word and checks if it is valid
    clue = checkAnswer (userInput, list(word))# gets the clues to use to update the voard
    board = changeBoard(board, clue, guess)# update the board
    if checkWin(userInput,answer) == True: # check the condition the win condition after a turn
      win = True#set win to equal to true so that you can send a win message
      guess += 1# add 1 to their guess
      displayBoard(board)# display their win
      break# break from the loop
    guess += 1# add 1 to their guess
    displayBoard(board)# display their win
  end(win,word,guess) # end the game (this is outside the while loop so it will do this once it reaches past the 6th guess
