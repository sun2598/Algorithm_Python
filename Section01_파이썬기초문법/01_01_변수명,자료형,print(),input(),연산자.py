'''
<변수명 규칙>
1. 영문과 숫자, _ 로 이루어진다.
2. 대소문자를 구분한다.
3. 문자나, _ 로 시작한다. (숫자로 시작 불가! ⭐️)
4. 특수문자를 사용한면 안된다. (&, % 등)
5. 키워드를 사용하면 안된다. (if, for 등)
'''

a = 1
A = 2
A1 = 3
# 2b = 3 -> 불가!
print(a, A, A1)
a, b, c = 3, 2, 1 # 기존 a값 바뀜
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a # 그냥 이렇게 무식하게 가능
print(a, b)

# <자료형>
a = 12345
print(type(a)) # <class 'int'>

a = 12.123456789123456789
print(a) # 12.123456789123457 -> 8byte가 넘어가서 끊김
print(type(a)) # <class 'float'>

a = 'student'
print(type(a)) # <class 'str'>


#===========================================================================
# <print()>
print("number")
a, b, c = 1, 2, 3

print(a, b, c) # 1 2 3 -> print()에 여러 변수 입력시 자동 띄어쓰기! (디폴트가 sep=' ' 인 셈)
print(a, b, c, sep='/') # 1/2/3 -> 각 변수의 구분자가 sep이 됨
print(a, b, c, sep='\n')

print(a) # print()은 끝에 자동 줄바꿈! (디폴트가 end='\n' 인 셈) 줄바꿈 안해주려면 end에 다른 동작 지정
print(b, end=' ')
print(c)


#===========================================================================
# <input()>

# 여러개의 변수 입력받기 : split()안에 입력한 것으로 구분지어서 변수 a, b를 입력받음 (2 3 입력함)
a, b = input("숫자를 입력하세요 : ").split() 
print(type(a)) # <class 'str'>
print(a, b) # 2 3
print(a + b) # 23 -> a와 b는 str이라서 연결연산자로 작동함!

# str -> int 변환
a = int(a)
b = int(b)
print(a + b) # 5

# 변수를 입력받음과 동시에 자료형 지정하기⭐️
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b) # 5

#============================================================================
# <연산자>
print(3 + 2) # 5
print(3 - 2) # 1
print(3 * 2) # 6
print(4 / 2) # 2.0 -> 나누기는 항상 float타입으로 리턴됨
print(3 // 2) # 1 -> 몫
print(3 % 2) # 1 -> 나머지
print(3 ** 2) # 9 -> 거듭제곱 (3^2)

a = 4.3 # float
b = 5 # int
c = a + b # float
print(type(c)) # <class 'float'> -> 범위가 더 큰 자료형으로 연산됨