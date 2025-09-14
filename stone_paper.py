import random 
guessing = ["stone", "paper", "scissors"]
print("Welcome to the SPS-Game!")
print("Type 'stone', 'paper','scissors' to play. Type 'quit' to stop")
# loops 
while True:
    user_choice = input("Your choice: ").lower()

    if user_choice =="quit":
        print("Thanks for playing! Goodbye")
        break
    if user_choice not in guessing:
        print("invalid choice! Please choose stone, paper, scissor.")
        continue

    computer_choice = random.choice(guessing)
    print(f"computer choose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "stone") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("you win!")
    else:
        print("you loose!")
