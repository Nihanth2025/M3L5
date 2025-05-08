import random
play=True
n=str(random.randint(1,15))
print("Guess the number between 1 to 15")
print("Game will end when you guess the correct number")

while play:
    guess=input("Enter your guess number: ")
    if n==guess:
        print("Correct guess")
        print("The number was",n)
        print("You won the game")
        break
    else:
        print("Wrong guess.Try again")