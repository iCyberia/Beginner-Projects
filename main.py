import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
       continue

    random_num = random.randint(0,2)
    # 0 rock, 1 paper, 2 scissors
    computer_pick = options[random_num]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("you win")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win")
        user_wins += 1
    else:
        print ("you loose")
        computer_wins += 1
print("you won", user_wins, "times")
print("computer won", computer_wins, "times")
print ("Good bye")
