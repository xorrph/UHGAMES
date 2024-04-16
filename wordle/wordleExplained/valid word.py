#valid word
# check if the word inputted by the user is a valid word, checked against a larger text file containing alot more words


def validWord(userInput): # userInput is passed as a parameter
  f = open("answerExplained.txt", "r")# open the file and assign it to the f variable
  content = f.readlines()# create an array called content containing each line as a seperate item 
  while True: # keep running this when it is called
    userInput  = " " + userInput + " " # format userinput correctly for when it is returned 
    for x in content: # for each line in content 
     if x.find(userInput) != -1: # if the word that the user entered is found
       return userInput.strip( )# return the stripped word( this is to strip it from the spaces and /n upon return 
        
    userInput = input(" Invalid word, enter a 6 letter word: ").lower()# after the for loop it will ask the user to enter a new word, and it will repeat this until it finds a word



# further explanations
# find function will return -1if the word being searched for is not found
# therefore I check if it has been found by checking if the returned value of the function is anything but -1
# return will not run anymore lines in the function hence why I have while True since I do not need a condition to check
# the actual code needs to strip /n since sometimes it will format wrong since when saved to contents it saves the new line at the end of each line of the text file


