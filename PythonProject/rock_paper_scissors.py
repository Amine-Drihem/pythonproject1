import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter a choice (rock, paper, or scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "paper":
        print("you win")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    else:
        print("you lose")

    play_again = input("play again ? (y or n):").lower()
    if play_again == "y":
        running = True
    elif play_again == "n":
        running = False
    else:
        print("enter a valid answer (y or n): ")
        play_again = input("play again ? (y or n):").lower()
        if not play_again == "y":
            running = False

print("ty for playing")