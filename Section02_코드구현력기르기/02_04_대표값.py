'''
대표값

N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1
10 
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1 
74 7

예제설명)
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 
여기서 점수가 높은 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.
'''

n = int(input())
a = list(map(int, input().split()))
# avg = round(sum(a) / n) # 소수 첫째자리에서 반올림. (round(0.1234, 2)) -> 0.12 => 이 방법 지양!
avg = int((sum(a) / n) + 0.5)
minGap = 21470000000 # int타입 최대 정수값

# 많이 사용하는 방법!⭐️ a라는 리스트의 index, value에 이렇게 접근
for index, score in enumerate(a): # index는 학생인덱스번호, score는 점수
    tmpGap = abs(score - avg) # abs(n) : n의 절대값
    if tmpGap < minGap:
        minGap = tmpGap
        maxScore = score # 최대점수
        answer = index + 1 # 학생번호
    elif tmpGap == minGap: # 절대값이 같은 경우
        if score > maxScore: # 점수가 높은 쪽이 답. (>= 로 등호 있을시 학생번호가 뒤인 쪽이 정답)
            maxScore = score
            answer =  index + 1
print(avg, answer)

#===================================================================================
# 파이썬에서 round는 round_half_even 방식! (<-> round_half_up)
# 정확히 중간 지점이면 짝수 쪽으로 감
x = 4.5000
print(round(x)) # 4 출력

# 그래서 round대신 0.5를 더하고 int형으로 형변환해주는 방식으로!⭐️ (int()하면 소수점 버림)
x = 67.5
x = x + 0.5
x = int(x)
print(x) # 68 출력