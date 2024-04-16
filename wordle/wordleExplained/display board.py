#display Board function
#using the previous funciton that initalised board we now try to display the board in a
#user friendly way 



def displayBoard(board): # pass in board as a parameter
  for row in board: # for each row in  the board ....
    grid = (" | ").join(row) #join each of the columns using " | " this and assign this to the grid variable
    print(" -------------------------") # seperate the top and bottom row using these ( i did trial and error to work out the board length)
    print((" | ") + grid + (" | ")) # concatenate the grid variable with " | " before and after it. these will act as the boarder around the inside of the grid 
  print(" -------------------------") # same thing again once the for loop ends 


board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']] # the intialised board variable
displayBoard(board) # calling the function
input()# stop the exe from closing

#when you run this code it will not look good in the IDLE shell due to it having different character lengths however if you go into file explorer and double click on this program
#it will run in the command prompt shell so all the characters will be of even length and it will look alot better and user friendly

#deeper explanation

#for each row access each 'row' in the board list
# [' ', ' ', ' ', ' ', ' ', ' '] will be accessed and it will then
# join each individual item together with a | 
# grid will become the string: " |   |   |   |   | " 
# these | represent the individual slots and where each letter - clue goes
# next you print the border to seperate each row
# and then you print the grid variable + the | on either side to act as the border on the side
# then you print the bottom border again once the for loop ends
