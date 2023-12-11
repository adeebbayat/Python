import random

y=0
counter = 0
while(y == 0):
    x = random.choice(["heads","tails"])
    if(x == "tails"):
        y = 1
    counter = counter + 1
    print(counter)