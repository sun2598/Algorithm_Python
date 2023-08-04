# <함수 만들기>

def add(a, b):
    c = a + b
    return c

print(add(3, 2)) # 5

def add(a, b):
    c = a + b
    d = a - b
    return c, d # 여러개 리턴 가능! -> 튜플 형태로 리턴

print(add(3, 2)) # (5, 1)


# 소수만 출력하는 함수 만들기
a = [12, 13, 7, 9, 19]
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True # 위에서 return되지 않는다면 여기에 올테니까

for x in a:
    if isPrime(x):
        print(x, end=' ') # 13 7 19 

print()
#===========================================================================
# <람다함수>
# = 익명함수 = 람다표현식

# 람다함수 사용 방법 1 
# (이 방법은 함수를 변수에 할당해줘야함)
plus_one = lambda x: x + 1 # x는 매개변수, x + 1를 리턴
print(plus_one(1)) # 2
a = [1, 2, 3]
print(list(map(plus_one, a))) # [2, 3, 4]
# map(함수명, 자료) : 자료에 함수 적용하여 리턴

# 람다함수 사용 방법 2 -> 주로 이 방법 사용!⭐️
print(list(map(lambda x: x + 1, a))) # [2, 3, 4]
