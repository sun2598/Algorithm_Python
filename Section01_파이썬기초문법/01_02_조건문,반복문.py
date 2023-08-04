# <조건문 if>

# if else 문
x = 15
if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")
    else:
        print("10 이상의 짝수")
else:
    print("10 미만의 자연수")

x = 9
if 0 < x < 10: # 파이썬은 이게 가능! (x > 0 and x < 10 이거랑 같음)
    print("0과 10 사이의 자연수") 

# if elif else 문
x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')

#===========================================================================
# <반복문 for, while>

# range( , ) : 마지막 인덱스 불포함!⭐️
a = range(10) # 10 불포함!
print(list(a)) # list타입으로 출력

# for문
for i in range(10):
    print(i, end=" ") # 0 1 2 3 4 5 6 7 8 9 
print()
for i in range(0, 10, 2): # 0 2 4 6 8 -> 마지막 인자만큼 더하거나 빼짐
    print(i, end=" ")
print()
for i in range(10, 0, -1): # 10 9 8 7 6 5 4 3 2 1 -> 마지막 인자만큼 더하거나 빼짐
    print(i, end=" ")
print()

# while문
i = 1
while i <= 10:
    print(i, end=" ") # 1 2 3 4 5 6 7 8 9 10 
    i = i + 1
print()
i = 10
while i >= 1:
    print(i, end=" ") # 10 9 8 7 6 5 4 3 2 1 
    i = i - 1
print()

# break, continue
i = 1
while True:
    print(i, end=" ") # 1 2 3 4 5 6 7 8 9 10 
    if i == 10: # 10이면 반복문을 벗어남
        break
    i += 1 # i = i + 1 과 같음
print()

for i in range(1, 11):
    if i % 2 == 0: # 짝수인 경우 skip, 반복문의 처음으로
        continue
    print(i, end=" ") # 1 3 5 7 9 
print()

# for else 문
for i in range(1, 11):
    print(i, end=" ") # 1 2 3 4 5 
    if i == 5:
        break
else:
    print(11) # 위에서 break를 안 당하고 정상 종료된다면 얘도 출력됨
print()

#===========================================================================
# <반복문을 이용한 문제풀이>

# 1. 1부터 n까지 홀수 출력하기 (10 입력)
n = int(input()) # input은 str로 들어오니까 형변환 필수!
for i in range(1, n+1):
    if i % 2 == 1:
        print(i, end=" ") # 1 3 5 7 9 
print()

# 2. 1부터 n까지의 합 구하기 (10 입력)
n = int(input())
sum = 0 # 초기화는 바깥에서!
for i in range(1, n+1):
    sum = sum + i
print(sum) # 55

# 3. n의 약수 출력하기 (10 입력)
n = int(input())
for i in range(1, n+1):
    if n % i == 0: # 나머지가 0이면 약수임
        print(i, end=" ") # 1 2 5 10 
print()
#===========================================================================
# 중첩반복문 (2중 for문)

for i in range(5):
    print('i:', i, end=' ')
    for j in range(5):
        print('j:', j, end=' ')
    print()

# 별찍기
for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

for i in range(5):
    for j in range(5 - i):
        print("*", end=' ')
    print()
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)