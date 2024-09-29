#1
a = input("입력:")
if a == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

#2
b = int(input("숫자입력:"))
result = b+100
if result >150:
    print(result)
else:
    print("값이 부족합니다.")

#3
numbers = [100,200,300]
c = []
for i in numbers:
    c.append(i+i*0.1)
print(c)

#4
numbers1 = [3,100,23,33,72,94]
d=[]
for i in numbers1:
    if i %3 ==0:
        d.append(i)
print(d)

#5
waiting_number = 1
while waiting_number <= 1000:
    print(f"대기번호: {waiting_number}")
    waiting_number += 1

#6
num = 1
sum_of_odds = 0
while num <= 100:
    if num % 2 == 1:
        sum_of_odds += num
    num += 1
print(f"1부터 100까지 존재하는 모든 홀수의 합: {sum_of_odds}")



