import random

cylinder = random.randint(1,6)
round = input("Pick a number between 1 to 6\n")
chance = int(round)
start = 1
while start <= 6:
    if chance == start:
        print("You have survived this round, The bullet was in " + str(cylinder) + " chamber")
        break
    elif chance < cylinder:
        print("You've pulled the trigger and but it seems the chamber is empty")
        start += 1
    elif chance >= cylinder:
        print("You were shot, the bullet was in the " + str(cylinder) + ". Better luck next time")
        break
    else:
        print("Error, Looks like they forgot to load the chamber! Oops!")
        break