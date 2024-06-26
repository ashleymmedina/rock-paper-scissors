# Play command line Rock-Paper-Scissors
# By: Ashley Meza

import random
# rps = ["rock", "paper", "scissors"]

player1_choice = input("Make your choice, Rock, paper or scissors: ")
player2_choice = input("Make your choice, Rock, paper, or scissors: ") #random.choice(rps)

if player1_choice == "rock":
    if player2_choice == "scissors":
        print("Player 1 won!")
    if player2_choice == "paper":
        print("Player 2 won")
    if player2_choice == "rock":
        print("You tied!")

if player1_choice == "scissors":
    if player2_choice == "rock":
        print("Player 2 won!")
    if player2_choice == "paper":
        print("Player 1 won!")
    if player2_choice == "scissors":
        print("You tied!")


if player1_choice == "paper":
    if player2_choice == "rock":
        print("Player 2 won!")
    if player2_choice == "scissors":
        print("Player 1 won!")
    if player2_choice == "paper":
        print("You tied!")

              



