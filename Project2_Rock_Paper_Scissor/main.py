import random

while True:
        choices = ["rock", "paper", "scissors"]

        computer = random.choice(choices)
        player = None

        while player not in choices:
                player = input("Rock, Paper, or Scissors?: ").lower()
        
        if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("Tie!")
        
        else:
                print("computer: ", computer)
                print("player: ", player) 
                match player:
                        case "rock":
                            if computer == "paper" :
                                   print("You Lose!")
                            else:
                                   print("You Win")
                        case "paper":
                            if computer == "scissors" :
                                   print("You Lose!")
                            else:
                                   print("You Win")
                        case "scissors":
                            if computer == "rock" :
                                   print("You Lose!")
                            else:
                                   print("You Win")
        play_again = input("Play again? (yes/no)").lower()
        if play_again != "yes":
               break
print("Bye!")