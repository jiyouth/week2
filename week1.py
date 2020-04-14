print('hello world')

a=10
b=3
c=b//a
print(a*b-c)

#변수
odd = [1,3,5,7,9]
#인덱싱
print('odd[0]:', odd[0])
#리스트 안의 리스트
odd1 = [1,3,7,9,['홀수','짝수','홀수1']]
print('odd1:',odd1)
print('odd1[4][2]:',odd1[4][2])
#리스트 슬라이싱
print('odd1[0:2]:',odd1[0:2])
#리스트 연산자
print('odd+odd1:',odd+odd1) #더하기
print('odd*3:', odd*3) #반복하기
#index 자리 반환
print('index.odd1[5]:',odd.index(5))
#리스트 요소 삭제
del odd1[1]
print('del odd1[1]:', odd1)

#딕셔너리 자료형
person = {'name':'이지윤','age':24,'hometown':'서울'}
#key
'name','age','hometown'
#value
'이지윤','24','서울'
#key 값을 통해 value 값 뽑아내기
print("person['name']:",person['name'])
#key 리스트 뽑아내기
print("person.keys()",person.keys())
#value 리스트 뽑아내기
print("person.values():",person.values())
#key값이 있는지 없는지 조사하기
print("'name' in person:",'name' in person)

# 1.if문
money = True
if money == True:
    print("고기 먹자")
else:
    print("학식 먹자")

# if 문제
a=int(input("숫차를 쳐주세요"))
b=a%2

if(b == 0):
    print('짝수입니다.')
else:
    print('홀수입니다.')    

#elif 문제
a=int(input("키를 입력해주세요:"))

if(a>185):
    print('tall')
elif(a<145):
    print('small')
else:
    print('regular')        

#for문
testList = ['one','two','three','four','five']

for i in testList:
    print(i)

#range함수
#숫자 리스트를 자동생성
# range(0,10) = 0,1,2,3,4,5,6,7,8,9
# 끝자리 숫자는 포함시키지 않는다!!

sum = 0
for i in range(1,11):
    sum = sum + i
    print(sum)