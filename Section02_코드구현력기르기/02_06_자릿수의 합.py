'''
자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 
각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력합니다.

▣ 입력예제 1 
3
125 15232 97

▣ 출력예제 1 
97
'''

n = int(input())
a = list(map(int, input().split()))
max = -2147000000

#============================================
# <방법1>
def digit_sum(x):
    sum = 0
    # 각 자리수의 합 구하는 법⭐️
    while x > 0:
        sum += x % 10 # 10으로 나눈 나머지
        x = x // 10 # 10으로 나눈 몫으로 갱신
    return sum

for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        answer = x

print(answer)
#============================================
# <방법2>
def digit_sum2(x):
    sum = 0
    for i in str(x): # 문자열로 변환
        sum += int(i)
    return sum

for x in a:
    total = digit_sum2(x)
    if total > max:
        max = total
        answer = x

print(answer)