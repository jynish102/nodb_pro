"""
WorkFlow Of Game:
1- Input From User(Rock, Paper, Scissor)
2- Computer Choice

Logics:
Cases:
A-Rock
Rock -Rock =Tie
Rock-Paper = Paper Wins
Rock-Scissor = Rock Wins

B-Paper
Paper-Rock = Paper Wins
Paper-Paper = Tile
Paper-Scissor = Scissor Wins

C-Scissor
Scissor -Rock = Rock Wins
Scissor-Paper=Scissor Wins
Scissor - Scissor = Tile
"""

import random
item = ["Rock", "Paper", "Scissor"]

User_Choice = input(f"Enter Your Choice from {item}: ")
Computer_Choice = random.choice(item)

print(f"User Choice = {User_Choice}, Computer Choice = {Computer_Choice}")

if User_Choice == Computer_Choice:
  print("Both Chooses Same Item: Match Tile")

elif User_Choice == "Rock":
    if Computer_Choice == "Paper":
     ("Paper Covers The Rock: Computer Win")
    else:
       print("Rock Smashes Scissor: You Win") 

elif User_Choice == "Paper":
    if Computer_Choice == "Rock":
     ("Paper Covers The Rock: You Win")
    else:
       print("Scissor Cut The Paper: Compute Win") 

elif User_Choice == "Scissor":
    if Computer_Choice == "Paper":
     ("Scissor Cut The Paper: You Win")
    else:
       print("Rock Smashes Scissor: Computer Win")        

