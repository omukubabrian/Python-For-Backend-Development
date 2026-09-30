import random
player=input("Input either Rock,Paper or siscors:")
computer=random.choice(["rock","paper","siscors"])

print("Computer choose:",computer)
if player==computer:
    print("It's a Draw")

elif player=="rock" and computer=="paper":
    print("You lose!")

elif player=="paper" and computer=="siscors":
    print("You lose!")

elif player=="siscors" and computer=="rock":
    print("You lose!")
else:
    print("Hurree!!!You win!")

