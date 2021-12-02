import random
computersChoice = ["rock", "paper", "scissor"]
wish = "yes"
print("WELCOME TO THE ROCK PAPER SCISSOR GAME (^_^)")
playerName=input("Enter your name: ")
while wish != "no":
    player = input("your choice(select rock, paper or scissor): ")
    computer = random.choice(computersChoice)
    if computer == player:
        print("DRAW")
    else:
        if computer == "rock" and player == "scissor":
           print("computer won the game!")
        elif computer == "paper" and player == "rock":
            print("computer won the game!")
        elif computer == "scissor" and player == "paper":
            print("computer won the game!")
        elif computer == "rock" and player == "paper":
            print("You won the game!")
        elif computer == "paper" and player == "scissor":
            print("You won the game!")
        elif computer == "scissor" and player == "rock":
            print("You won the game!")
    wish = input("Do you want to continue?(yes/no): ")
print("WELL PLAYED", playerName.upper()+"!.""THANKS FOR PLAYING!(^_^)")  

