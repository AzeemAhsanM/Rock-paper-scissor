import random

computer_wins = 0
user_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type 'rock', 'paper', 'scissor' or q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer pick:",computer_pick +".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("picked the same, TRY AGAIN!")
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("you won1", user_wins, "times")
print("the computer won", computer_wins, "times")
print("End of th e Game")


