# This is a guess the number game
import random

print("Hello. What is your name?")
name = input()

print(" Well, " + name + ", I am thinking a number between 1 and 20. ")
secretnumber = random.randint(1, 20)
try:
    for guessesTaken in range(1, 7):
        print("Take a guess")
        guess = int(input())

        if guess < secretnumber:
            print("Your guess is too low.")
        elif guess > secretnumber:
            print("Your guess is to high.")
        else:

            break  # This condition is for the correct guess!
except:
    ValueError
print("You did not enter a number!")

if guess == secretnumber:
    print(
        "Good job, "
        + name
        + "! You guessed my number in "
        + str(guessesTaken)
        + " guesses!"
    )
else:
    print("Nope. The number I was thinking of was " + str(secretnumber))
