#Computer picks at random(0-100)The player guesses until correct.After each guesss,say"Too low"or "Too high".Count the guesses
import random
secret=random.randint(1,100)
guesses=0
print("I'm thinking of a number between 1 and 100.")
while True:
    guess_text=input("Your guess: ")
    guess=int(guess_text)
    guesses+=1

    

    if guess<secret:
     print("Too low")
    elif guess>secret:
     print("Too high")
    else:
     print(f"Correct! You needed {guesses} guesses.")
    break