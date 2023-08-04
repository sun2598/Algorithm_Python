# <문자열과 내장함수>

# upper(), lower()
msg = "It is Time"
print(msg.upper()) # IT IS TIME -> msg 자체를 바꾸는 건 아님!
print(msg.lower()) # it is time
print(msg) # It is Time -> 원본은 그대로 보존

# find(), count()
tmp = msg.upper()
print(tmp) # IT IS TIME
print(tmp.find('T')) # 1 -> 'T'의 첫번째 인덱스번호. (없으면 -1 리턴)
print(tmp.count('T')) # 2

# [ : ] 를 통한 slice (마지막 인덱스 불포함!⭐️) -> 원본 문자열엔 영향 없음!
print(msg) 
# It is Time
# 0123456789
print(msg[:2]) # It -> 0,1 인덱스
print(msg[3:5]) # is -> 3,4 인덱스

# 문자열 접근 방법 1
print(len(msg)) # 10 -> len()으로 길이 구하기
for i in range(len(msg)):
    print(msg[i], end=' ') # I t   i s   T i m e -> msg[i] 이렇게 인덱스로 접근
print()
# 문자열 접근 방법 2
for x in msg:
    print(x, end=' ') # I t   i s   T i m e 
print()

# isupper(), islower() : 대문자/소문자 여부 True/False 리턴
for x in msg:
    if x.isupper():
        print(x, end=' ') # I T 
print()
for x in msg:
    if x.islower():
        print(x, end=' ') # t i s i m e 
print()

# isalpha() : 알파벳인지 여부 True/False 리턴
for x in msg:
    if x.isalpha():
        print(x, end=' ') # I t i s T i m e 
print()

# <ASCII 번호>
# 0 ~ 9 : 48 ~ 57
# A ~ Z : 65 ~ 90
# a ~ z : 97 ~ 122
# ord() : 해당 문자에 대한 ASCII 번호 리턴
tmp = '09AZaz'
for x in tmp:
    print(ord(x), end=' ') # 48 57 65 90 97 122 

# chr() : 해당 ASCII 번호에 대응하는 문자 리턴
print(chr(65)) # A
