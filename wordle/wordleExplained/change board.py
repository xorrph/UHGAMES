#change board
#this is a small and simple function, it is used to update the board with your new clues


def changeBoard(board, clue, guess):# parameters are passed in
  for letter in range(6): # add the new word to the board
    board[guess][letter] = clue[letter]#the guesses are the rows and each letter are the columns,
    # they are then assigned to be the same as the clue in that index position
  return board # return the updated board


#visualisation



##           0    1    2    3   4   5
##         [                                     These outside brackets are for defining the entire board
##    0   [" " ," " ," " ," " ," " ," "],   The inside brackets are for defining each row
##    1   [" " ," " ," " ," " ," " ," "],
##    2   [" " ," " ," " ," " ," " ," "], 
##    3   [" " ," " ," " ," " ," " ," "],
##    4   [" " ," " ," " ," " ," " ," "], 
##    5   [" " ," " ," " ," " ," " ," "],
##         ]

#guess = 0
#letter = 0
#clue = ["+","?","+","-","-","+"]

##        [0]
#clue[letter] - > "+"

#therefore in the board it will change to this

##              letter  -->
##                 [0]   1    2    3   4   5
##             [                                
##  g    [0]  ["+" ," " ," " ," " ," " ," "],   
##  u     1    [" " ," " ," " ," " ," " ," "],
##  e     2    [" " ," " ," " ," " ," " ," "], 
##  s     3    [" " ," " ," " ," " ," " ," "],
##  s     4    [" " ," " ," " ," " ," " ," "], 
##   |     5    [" " ," " ," " ," " ," " ," "],
##  \/        ]
