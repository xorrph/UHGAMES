# random word
# select a random word from a text file containing common 6 letter words
import random # import the random library

def randomWord(): 
    file = open("answerExplained.txt", "r") #assign the opened file called 'answer.txt' in read only mode( indicated by the r) to the file variable
    content = file.readlines() # assign the contents of file to the content variable
    x = random.randint(0,len(content) - 1)# select a random index between 0 and the length of the content that was assigned and -1 because of how index works
    word = content[x] # assign the random word to be the word at the random index position within content
    return word# return the word



print(randomWord())# print returned word

#Note the actual game I used a word list I found online that contains more common words, the actual word list is alot longer since i tried to find a word list that includes as many words as possible

#more in depth

#content is assigned to be array containing each line in a new index position therefore
#in this example I have made the random index position that is chosen to showcase what word gets chosen for example if 3 is chosen then word3 will be shown

#in the text file 

##word0
##word1
##word2
##word3
##word4
##word5
##word6
##word7
##word8
##word9

#in the array
#    0            1           2          3           4           5           6          7            8          9          index positions
#[word0, word1, word2, word3, word4 ,word5 ,word6 ,word7, word8, word9]

# length 10

#despite the length of the array being 10 when choosing the random index I have to minus 1 on the length since the randint function
#is inclusive and index starts at 0 not 1 so the last value will be at position 9 and not 10

