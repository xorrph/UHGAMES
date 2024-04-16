# check answer
#this function goes through the word and compares the users word and answer to calculate what clues to return

def checkAnswer(userInput, answer):
    clue =["","","","","",""] # initialise the clue variable
    for index in range(len(userInput)):#iterates through the index positions of the length of the users word 
        if userInput[index] == answer[index]:#check if the letter is in the same place
          answer[index] = ("@")# this accounts for duplicate letters making sure the clues given are accurate
          clue[index] = ('+')#correct place
    for index in range(len(userInput)):#iterates through the index positions of the length of the users word 
          if userInput[index] in answer and answer[index] != "@":
              answer[answer.index(userInput[index])] = ("!")# this accounts for duplicate letters making sure the clues given are accurate
              clue[index] = ("?")#in the word not correct place
          elif userInput[index] not in answer and answer[index] != "@":
              clue[index] = ("X")#letter is not in the word
    return clue #returns the clue

print(checkAnswer("messed", list("mousse")))

#more in depth

#for this example I will use the answer word as 'mousse' and the users guess as 'messed'

# the program first goes through each word and places
# it does this by comparing at the same index positions and then changing the index position of the clue variable to a + to symbolise it is correct
# the code also replaces the letter to a @
# this acts a placeholder to cross of which letteres have been marked off as placed

#after the answer and clue variables should look like this

#answer: @ous@e
#clue: ["+","","","","+",""]

#next the code will go through and redo the loop but this time to find if the current letter is in the word
#if it is it will assign the first letter that it finds a ! which crosses it off in the answer word
#this is so that if a letter is if  the answer has two or more letters that are the same it wont reveal all of them and will only reveal them if your word also has that amount of the same letters
# for example if the answer was 'mining' and you guessed 'triads' it should only reveal the first i as being yellow and not the last one unless your guess something like 'icicle'
# answer[answer.index(userInput[index])]  this line looks complex but it is simple;
# userInput[index] retrieves the current letter that the for loop is on
# the .index() function retrieves the index position of the first appearance of the value that is passed in as a parameter
# then it uses this index position to change the values within the answer to have ! to account for repeated letters
#then the elif deals with the othercase and making sure that the greens are not treated as wrong clues

#now the answer and clue should look like this

#answer: @ou!@!
#clue: ['+', '?', '?', '+', 'X', 'X']

#it loops twice because if a word is found to be correct it can be changed back to ? again or X so I developed a method to prioritise sorting out the correct clues first and then deal with the other cases
