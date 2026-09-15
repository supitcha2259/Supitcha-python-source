"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random 

secret_number = random.randint(1,20)
        
for i in range(1,7):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            break
        
        except ValueError:
            print("Please enter a number only.")
            
    if guess == secret_number:
        print(f"Congratulations! You won in {i}/6 attempt!")
        break
            
    elif guess > secret_number:
        print(f"Too high! Try again.")
        print(f"You have used this many rounds: {i}/6 attempt.")
     
    else:
        print(f"Too low! Try again.")
        print(f"You have used this many rounds: {i}/6 attempt.")
    
if i == 6 and guess != secret_number:
    print("You lose.")
    
else:
    print(f"You win.")
