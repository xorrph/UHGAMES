# end

#the end of the game
#simple function using if, else and input

def end(win,answer,guess): #end of game
  if win == True:# if they won, it congratulates the player and tells them in how many tries
    print(" Congratulations, you won in {} tries".format(guess)) #the variable guess is put within the {} 
  else:
    print(" You lost, the word was {}, better luck next time!".format(answer.strip()))#he stripped answer is put within the {} 
  yn = input(" Do you want to play again (Y/N)? ")#asks the user to play again
  if yn.upper() == "Y":# checks if they entered Y
    main() #starts the game again by calling the main function
  else:
    input(" Thanks for playing!")#prints thanks for playing
