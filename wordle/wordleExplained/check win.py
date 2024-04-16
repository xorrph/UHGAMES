# check win
#simple code to check for a win


def checkWin(userInput,answer):#check if the word has been guessed
  if userInput == answer:# check if the users word is equal to the answer
    return True# if so return True
  else:
    return False# else return False

