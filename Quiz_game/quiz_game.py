'''This is a simple quiz game,
that takes a user input and award the user for a correct answer
and also deduct a point for a wrong answer.'''

print("welcome to the Quiz!")
#taking input from the user 
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print(""" 
    The rules of the game are very simple. \n
    One correct answer awards you with a point \n
    One wrong answer deduct you a point, so be careful!\n 
    Okay! Let's play :)""")
score = 0 

answer = input(" Question 1: \n What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    score -= 1

answer = input("Question 2: \n What does IP stand for? ").lower()
if answer == "internet protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    score -= 1

answer = input(" Question 3: \n What does VPLS stand for? ").lower()
if answer == "virtual private leased service":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    score -= 1

answer = input(" Question 4: \n What does MPLS stand for? ").lower()
if answer == "multi-protocol label switching":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    score -= 1

answer = input(" Question 5: \n What does HSRP stand for? ").lower()
if answer == "hot stand-by redundancy protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    score -= 1

print ("Your total score is " + str((score/ 5) * 100) + "%")


