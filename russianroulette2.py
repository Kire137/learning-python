from numpy import random

input("russian roulette! enter a number 1-6: ")

if random.randint(6)!=1:
    print("lucky you, not dead yet")
else:
    print("you fucking died.")
    # sys.delete "system32"