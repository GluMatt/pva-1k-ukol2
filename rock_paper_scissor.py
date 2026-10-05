import random
computer_score = 0
player_score = 0
a = ["rock", "scissors", "paper"]
while True:
    computer_move = random.choice(a)
    player = input("rock, paper, scissors or end game?")
    if player not in ["rock", "paper", "scissors", "end game"]:
        print("error")
    if computer_move == player:
        print("tie")
    elif computer_move == "rock" and player == "paper" or computer_move == "paper" and player == "scissors" or computer_move == "scissors" and player == "rock":
        print("you won this round")
        player_score += 1
    elif computer_move == "rock" and player == "scissors" or computer_move == "paper" and player == "rock" or computer_move == "scissors" and player == "rock":
        print("you lost this round")
        computer_score += 1
    if player == "end game":
        print(computer_score, ":", player_score)