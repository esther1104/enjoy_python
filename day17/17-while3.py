dan = 1

while dan<=9:
    x=1
    while x <= 9:
        strDan=str(dan)
        strX=str(x)
        strValue=str(dan*x)
        print(strDan + "X" + strX + "=" + strValue)
        x=x+1
    dan=dan+1
    
print("end")

print("-----Homework-----")

D=1

for D in range(1,10):
    Y=1
    for Y in range(1,10):
        strD=str(D)
        strY=str(Y)
        strV=str(D*Y)
        print(strD + "X" + strY + "=" + strV)
        x=x+1
    D=D+1
