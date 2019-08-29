strScore=input("점수를 입력하세요.")

score=int(strScore)

if score>100:
    print("잘못된 점수입니다.")
    
elif score>=90:
    print("A 학점입니다.")
    
elif score>=80:
    print("B 학점입니다.")

elif score>=70:
    print("C 학점입니다.")

elif score>=60:
    print("D 학점입니다.")

elif score<0:
    print("잘못된 점수입니다.")

else:
    print("F 학점입니다.")

