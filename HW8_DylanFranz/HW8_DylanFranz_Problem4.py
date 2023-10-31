"""
Dylan Franz
CS 100 2023F Section H09
HW 08, November 1, 2023
"""
import random

print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
randomNumber = random.randrange(0,50)
count = 1
while count < 6:
    guess = input("Guess " + str(count) + "? ")
    if int(guess) == randomNumber:
        print("You are right! I was thinking of " + str(randomNumber) + "!")
        break
    elif int(guess) > randomNumber:
        print(guess + " is too high")
    elif int(guess) < randomNumber:
        print(guess + " is too low")
    count += 1
    if count == 6:
        print("Sorry you didn't guess it but my number was " + str(randomNumber))
