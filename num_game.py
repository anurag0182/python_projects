import random

random_number = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100...!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.") 
        else:
            print(f"Congratulations!!! you guessed it! the number is {random_number}.")
            break 
    except ValueError:
        print("Please enter a valid number.")