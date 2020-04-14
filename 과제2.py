height=int(input("키를 cm로 입력해 주세요:"))
weight=int(input("몸무게를 kg으로 입력해 주세요:"))
bmi = weight/((height/100)**2)

if(bmi<=18.5):
    print('저체중')
elif(bmi<23):
    print('정상체중')
elif(bmi<25):
    print('과체중')
elif(bmi<30):
    print('비만')    
else:
    print('고도비만')
