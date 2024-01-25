This Python code is a simple implementation of a rock-paper-scissors game against the computer. Here's a breakdown of how the code works:

1. **Initialization:**
   - a counter for user wins (`user_wins`) and computer wins (`computer_wins`).
   - define a list (`options`) containing the possible choices: "rock," "paper," and "scissors."

2. **Game Loop:**
   - The program enters an infinite loop (`while True`), allowing the user to play the game multiple times.

3. **User Input:**
   - The user is prompted to choose "rock," "paper," "scissors," or type "Quit" or "q" to exit. The input is converted to lowercase for case-insensitive matching.

4. **Handling Quit Command:**
   - If the user types "q" or "quit," the program breaks out of the loop, ending the game.

5. **Validation of User Input:**
   - If the user's input is not a valid choice, the program continues to the next iteration of the loop without processing the invalid input.

6. **Random Computer Choice:**
   - The program generates a random number (0, 1, or 2) to represent the computer's choice of "rock," "paper," or "scissors."

7. **Determining the Winner:**
   - The user's choice and the computer's choice are compared, and the winner is determined based on the rules of rock-paper-scissors.
   - If the user wins, a message is printed, and the user wins counter is incremented.
   - If the user loses, a message is printed, and the computer wins counter is incremented.

8. **Game Statistics and Exit:**
   - After the user decides to quit, the program prints the number of times the user won and the number of times the computer won.

9. **End of the Program:**
   - The program prints a farewell message ("Goodbye") before exiting.

Overall, the code creates a simple rock-paper-scissors game where the user can play against the computer multiple times until choosing to quit.