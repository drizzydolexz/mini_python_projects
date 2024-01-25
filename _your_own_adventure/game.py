import random

def play_game():
    name = input("Hello! Welcome to the Kismet game!\nWhat is your name? ")
    print("Wanderer", name, "your adventure begins now!")

    score = 0

    # Initial choice
    choice = input(
        "You are on a dirt road, it has come to an end.\nYou can choose to go right or left, which way do you want to go? "
    ).lower()

    if choice == "left":
        # Scenario 1: River
        choice = input("You have come to a river, you can walk around it or swim across.\nDo you want to swim or walk? ").lower()

        if choice == "swim":
            print("You bravely swim across the river.")
            score += 10
        elif choice == "walk":
            print("You safely walk around the river.")
            score += 5
        else:
            print("Not a valid option. You lose.")

    elif choice == "right":
        # Scenario 2: Bridge
        choice = input("You have come to a bridge, it looks wobbly.\nDo you want to cross or go back? ").lower()

        if choice == "cross":
            if random.choice([True, False]):
                print("You cross the bridge successfully.")
                score += 10
            else:
                print("The wobbly bridge collapses! You lose.")
                return
        elif choice == "back":
            print("You wisely decide to go back.")
            score += 5
        else:
            print("Not a valid option. You lose.")

    print("As you continue your journey, you encounter a mysterious cave.")

    # Scenario 3: Cave
    choice = input("Do you want to enter the cave or ignore it? ").lower()

    if choice == "enter":
        print("Inside the cave, you find a hidden treasure! You win!")
        score += 20
    elif choice == "ignore":
        print("You decide not to enter the cave. The journey continues.")
    else:
        print("Not a valid option. You lose.")

    print("Your adventure ends. Thank you for playing,", name)
    print("Your final score is:", score)

# Run the game
play_game()
