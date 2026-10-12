import random
num = int(input("Guess a Number from one to 10 :"))
goal = random.randint(1,10)
if num == goal:
    print("You Win")
    print("The Number was :",goal)
else:
    print("You Lost")
    print("The Number was :",goal)