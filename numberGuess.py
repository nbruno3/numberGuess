import math
import random
from os import system, name
import time
import sys

# A quick game (the first game) I created as I was/am learning Python...
# Fairly basic but takes advantage of the creation of functions, making calls,
# And checking user inputs for the correct values.

# I left in a lot of the code I first wrote, but have updated it to make it more concise.

# define our clear function 
def clearScreen(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(os.name is 'posix') 
    else: 
        _ = system('clear')

#Ask the user what range of numbers to guess between
def howManyNumbers():
    totalNumber = input("Pick your range of numbers to guess from! 1 to (max 1000): ")
    while totalNumber not in str(list(range(2,1001))):
        totalNumber = input("Dude, c'mon... Pick a number from 2 to 1000 already: ")
        
    totalNumber = int(totalNumber)
    return totalNumber

#Generate random number based on howManyNumbers() function
def generateRandNum(totalNumber):
    randNumber = random.randint(1,totalNumber)
    return randNumber

#Ask the user to guess a number and do some error checking, too
def askForNum(totalNumber):
    userGuess = input("Guess a number from 1 to %d: "%totalNumber)
    
    # OLD
    # #Check that user input a number and not other character
    # check = 1
    # while check == 1:
    #     try:
    #         val = int(userGuess)
    #         check = 0
    #     except ValueError:
    #        print("That's not a number! Try again!")
    #        userGuess = raw_input("Guess a number from 1 to 10: ")
    
    while userGuess not in str(list(range(1,totalNumber+1))):
        userGuess = input("Dude, c'mon... Guess a number from 1 to %d already: "%totalNumber)
     
    userGuess = int(userGuess)

    # OLD
    # #Once input is verified, check to make sure it is within bounds
    # while userGuess < 1 or userGuess > 10:
    #     print("That's not between 1 and 10! Try again!")
    #     userGuess = (raw_input("Guess a number from 1 to 10: "))
    #     check = 1
    #     while check == 1:
    #         try:
    #             val = int(userGuess)
    #             check = 0
    #         except ValueError:
    #            print("That's not a number! Try again!")
    #            userGuess = raw_input("Guess a number from 1 to 10: ")
    #            
    #     userGuess = int(userGuess)
    
    return userGuess

#Check users input vs randomly generated number
def checkAns(userGuess, randNumber):
        if userGuess == randNumber:
            return "Congratulations! You did it!"
        elif userGuess > randNumber:
            return "Guess lower!"
        else:
            return "Guess higher!"

#Throw it all together
def main():
    totalNumber = howManyNumbers()
    randNumber = generateRandNum(totalNumber)
    userGuess = askForNum(totalNumber)
    message = checkAns(userGuess, randNumber)

    #Keep the user guessing till they get it right!
    while message != "Congratulations! You did it!":
        print(message)
        new = askForNum(totalNumber)
        while new == userGuess:
            print("That's the same number - try again!")
            new = askForNum(totalNumber)

        userGuess = new
        message = checkAns(userGuess, randNumber)

    #Ask user if they'd like to play again!
    print(message)
    ans = input("Would you like to play again (y/n)? ")
    
    while ans != "y" and ans != "n":
        ans = input("Please enter 'y' or 'n' to continue: ")

    if ans == "y":
        main()
    elif ans == "n":
        print ("Thanks for playing!")

#Introduce ourselves, and play the game! And see how much time it was played for
if __name__ == "__main__":
    clearScreen()
    print("Welcome to our guessing game!")
    print("Press 'Ctrl-c' at any time to quit.")
    startTime = time.time()
    try:
        main()
    except KeyboardInterrupt:
        print("\nThanks for playing!")
        endTime = time.time()
        totalTime = endTime - startTime
        print("You played for %d seconds." %totalTime)
        sys.exit()
    endTime = time.time()
    totalTime = endTime - startTime
    print("You played for %d seconds." %totalTime)
