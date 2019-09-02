import random

while True:
    dice=random.randint(1,6)
    if dice == 6:
        print("6을 만나서 프로그램을 종료시킵니다.")
        break
    print(dice)

print("-----Homework-----")

x=1

while x <= 100:
    strX = str(x)
    print(strX)
    x=x+1
    if x == 50:
        print("숫자 50을 만나서 프로그램을 종료합니다.")
        break


    
