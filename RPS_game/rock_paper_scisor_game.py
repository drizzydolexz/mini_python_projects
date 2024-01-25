import random

user_wins = 0
computer_wins = 0

options =["rock","paper","scissors"] #list to have our options to pick from

while True:
    user_pick = input("Choose or type Rock/Paper/Scissors/Quit or q ?").lower()
    if user_pick == "q" or user_pick == "quit":
            break
    if user_pick not in ["rock","paper", "scissors"]:
          continue
    
    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_pick == "rock" and computer_pick == "scissors":
          print("You won!")
          user_wins += 1
          continue
    
    elif user_pick == "paper" and computer_pick == "rock":
          print("You won!")
          user_wins += 1
    
    elif user_pick == "scissors" and computer_pick == "paper":
          print("You won!")
          user_wins += 1
    else:
          print("You lost!\nComputer wins.")
          computer_wins += 1

print("You won " , user_wins, "times against computer")
print("The computer won " , computer_wins, "times against you")
print("Goodbye")
    
        
