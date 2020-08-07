# This is a guess-the-number game

import random
name = input("Hello, what is your name? ")
secretNumber = random.randint(1, 20)

print("Hi, " + name + ", I'm thinking of a number between 1 and 20.")

userinp = ''

while True:
    userinp = input("Guess a number between 1 and 20: ")
    
    try:
        userinp = int(userinp)
    except ValueError:
        print("That's not a number.")
        continue
    if userinp < 1 or userinp > 20:
        continue
    elif userinp > secretNumber:
        print("Too high!")
    elif userinp < secretNumber:
        print("Too low!")
    elif userinp == secretNumber:
        print("You got it! The number was " + str(secretNumber) + "!")
        break
    else: print("Something impossible just happened.")

