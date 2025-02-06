#rock paper scissors game

import random #library

def greeting():
    return "Hi! Welcome to the fatty game"

#call the function and prints.
response = greeting()
print(response)

#functions
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"] #list
    computer_choice = random.choice(options)
    #dictionary in the function
    choices = {"player" : player_choice, "computer" :  computer_choice}
    return choices

choices = get_choices()
print(choices)



def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie"
    elif player == "rock" and computer == "scissors":
        return "You beat the computer! You Win!"
    elif player == "rock" and computer == "paper":
        return "You lost to the computer! You lose!"


#check_win("rock", "paper")


