# A simple number guessing game
# Could you make something cooler?
import random

# Make n a random number between 1 and 99
n = random.randint(1, 10)

# Ask user to guess the number
guess = int(input("Enter an integer from 1 to 10: "))

while True:
    if guess >= 1 or guess <= 10 :
        if guess < n or guess > n : 
            print ("try again")
            guess = int(input("Enter an integer from 1 to 10: "))
        else:
            print ("you guessed it!")
            break

