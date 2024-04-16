#Make Board function
#This function is used to initalise the board using arrays
#The board will be used to display the clues based on each entered word


def makeBoard(width,length): # a funciton is used to pass in the width and length parameters
  empty = " " # empty is defined
  board = [] # the board variable is initalised
  for i in range(length): # now we make a for loop and in each iteration it will create each row and  their columns
     board.append([empty] * width) #this will append the rows with the columns within the row, the columns are defined by the empty * width
  return board # after the for loop is finished we return the board




b = makeBoard(6,6)# call the function and pass in the parameters
print(b)# the array representation is printed


#visaulised output

#board.append([empty] * width)
#[" "] will be repeated width amount of times
#in this case 6 times
#[" "] [" "] [" "] [" "] [" "] [" "] -> each of these will be columns
#next we add all of these to the board list
#[" " ," " ," " ," " ," " ," "] -> this represents the first row and each column
# each column seperated by a comma for another index position
##           0    1    2    3   4   5
##         [                                     These outside brackets are for defining the entire board
##    0   [" " ," " ," " ," " ," " ," "],   The inside brackets are for defining each row
##    1   [" " ," " ," " ," " ," " ," "],
##    2   [" " ," " ," " ," " ," " ," "], 
##    3   [" " ," " ," " ," " ," " ," "],
##    4   [" " ," " ," " ," " ," " ," "], 
##    5   [" " ," " ," " ," " ," " ," "],
##         ]
# each number represents the index position
# after the loop and adding each row the board visualised should look like this
# 6 guessses for 6 letter words
# key things to note are that the rows are the guesses and the columns are for the letters
