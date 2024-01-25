
import random

top_of_range = input( "Type a number: ")

#checks if the user input is an integer if false it converts it to a digit.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than zero next time.")
        quit()

else:
    print('Please type a number next time')
    quit()

random_number = random.randint(0, top_of_range)

#This loop ask the user to guess the number multiple times until it guess the correct random number.
guess = 0

while True:
    guess += 1 #this tracks the number of times you guessed to get the number correct.
    user_guess = input("Make a guess of the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time. ")
        continue # this sends the user back to the begining of the loop to make another guess if wrong or user did not type a number.

    if user_guess == random_number:
        print("You are a genius! \nYou guessed the right number!")
        print("You got the number right in " + str(guess) + " guesses") 
        break

    elif user_guess > random_number:
        print("you are above the number ")
    
    else: 
        print ("you were below the number")

