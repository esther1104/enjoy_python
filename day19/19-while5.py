import random

count = 1

while count <= 10:
    dice = random.randint(1,6)
    if dice == 3:
        print("빵")
        continue
    print(dice)
    count=count+1

