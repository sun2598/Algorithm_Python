# <리스트와 내장함수>
import random as r

# (예시)
#     0  1  2  3    -> 인덱스
# a : 90 72 55 83

# 빈 리스트 만드는 방법 2가지
a = []
b = list()
print(a) # []
print(b) # []

# 리스트 초기화 방법 2가지
a = [1, 2, 3, 4, 5]
b = list(range(1, 6))
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]

# 리스트 합치기
c = a + b
print(c) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# append() : 리스트 맨 뒤에 추가
a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]

# insert(i, n) : i번 인덱스에 n 추가
a.insert(3, 7)
print(a) # [1, 2, 3, 7, 4, 5, 6]

# pop() : 마지막 인덱스 삭제
a.pop()
print(a) # [1, 2, 3, 7, 4, 5]
# pop(i) : i번 인덱스 삭제
a.pop(3)
print(a) # [1, 2, 3, 4, 5]

# remove(n) : n이라는 요소 삭제
a.remove(4)
print(a) # [1, 2, 3, 5]

# index(n) : n이라는 요소의 인덱스 번호 리턴
print(a.index(5)) # 3


a = list(range(1, 11))
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sum(a) : a라는 리스트의 합
print(sum(a)) # 55

# max(a) : a의 인자들 중 가장 큰 값
print(max(a)) # 10
print(max(3, 5)) # 5
# min(a) : a의 인자들 중 가장 작은 값
print(min(a)) # 1

# random.suffle(a) : a를 랜덤으로 섞기
r.shuffle(a)
print(a) # [4, 1, 10, 8, 2, 3, 9, 5, 6, 7]

# sort() : 오름차순으로 정렬
a.sort()
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sort(reverse=True) : 내림차순으로 정렬
a.sort(reverse=True)
print(a) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# clear() : 리스트 값 다 없애기
a.clear()
print(a) # []

#===========================================================================
a = [23, 12, 36, 53, 19]

# [ : ] 를 통한 slice (마지막 인덱스 불포함!⭐️) -> 원본 리스트엔 영향 없음!
print(a[:3]) # [23, 12, 36] -> 0, 1, 2 인덱스
print(a[1:4]) # [12, 36, 53] -> 1, 2, 3 인덱스
print(a[ : :-1]) # [19, 53, 36, 12, 23] -> 역순으로 만들기!

# 리스트 접근 방법 1
print(len(a)) # -> len()으로 길이 구하기
for i in range(len(a)):
    print(a[i], end=' ') # 23 12 36 53 19 -> a[i] 이렇게 인덱스로 접근
print()
# 리스트 접근 방법 2
for x in a:
    print(x, end=' ') # 23 12 36 53 19 
print()
# 리스트 접근 방법 3
for x in enumerate(a): # enumerate는 튜플 형태로 접근! -> x가 튜플 타입이 됨
    print(x, end=' ') # (0, 23) (1, 12) (2, 36) (3, 53) (4, 19) 
print()

# <튜플>
# -> 리스트와 다른 점 : 변경 불가능!⭐️
b = (1, 2, 3, 4, 5)
# b[0] = 10 -> 에러남!

for x in enumerate(a):
    print(x[0], x[1])
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19

for index, value in enumerate(a): # 많이 사용하는 방법!⭐️ a라는 리스트의 index, value에 이렇게 접근
    print(index, value)
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19

# all() : 모든 조건이 True여야 True 리턴
if all(x < 60 for x in a):
    print("True")
else:
    print("False")

# any() : 한 조건이라도 True면 True 리턴
if any(x < 15 for x in a):
    print("True")
else:
    print("False")

#===========================================================================
# <1차원 리스트>
a = [0] * 3
print(a) # [0, 0, 0]

# <2차원 리스트>
# _ 사용시 변수 없이 반복문만 돎
a = [[0] * 3 for _ in range(3)] # [0] * 3 이라는 반복문이 3번 돌음
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[0][1] = 1
a[1][1] = 2
print(a) # [[0, 1, 0], [0, 2, 0], [0, 0, 0]]
'''
    0  1  2
   ---------
0 | 0  1  0
1 | 0  2  0
2 | 0  0  0
'''

# 표의 형태로 출력하는 방법 1
for x in a: # 여기서 x는 각각의 1차원 리스트임!
    print(x)
# [0, 1, 0]
# [0, 2, 0]
# [0, 0, 0]

# 표의 형태로 출력하는 방법 2
for x in a:
    for y in x:
        print(y, end=' ')
    print()
# 0 1 0 
# 0 2 0 
# 0 0 0 