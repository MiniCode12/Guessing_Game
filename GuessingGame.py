#Random number guessing game
from random import randint
num=randint(1,100)
cnt=1
print("Welcome to random number guessing game")
print("Guess the number between 1 to 100")
while True:
    print()
    guess=int(input("Guess the number : "))
    if guess==num:
        print("You guessed it right!! You Won!!")
        print("Number of attempts : ",cnt)
        break
    elif guess<1 or guess>100 :
        print("The number is not in the range")
    elif guess>num:
        if guess-num>=10:
            print("Too high! Try again")
        else:
            print("Guess a bit lower")
    else:
        if num-guess>=10:
            print("Too Low! try again")
        else:
            print("Guess a bit higher")
    cnt+=1
