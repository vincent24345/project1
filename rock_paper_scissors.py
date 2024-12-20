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


