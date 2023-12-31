'''
수들의 합

N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다. 
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

▣ 출력설명
첫째 줄에 경우의 수를 출력한다.

▣ 입력예제 1 
8 3 
1 2 1 3 1 1 1 2

▣ 출력예제 1 
5
'''

n, m = map(int, input().split())
list = list(map(int, input().split()))

sum = list[0]
cnt = 0
lt = 0
rt = 1

# <two pointer algorithm> 시간복잡도 O(n)
# sum : lt ~ rt(rt 불포함⭐️) 까지의 부분수열의 합. 처음엔 list[0] 대입
# 1  2  1  3  1  1  1  2   -> sum = 1, sum < m이니까 rt += 1
# lt rt
# 1  2  1  3  1  1  1  2   -> sum = 3, sum == m이니까 lt += 1(이제 sum==m이 될 일은 없으니까)
# lt    rt
# 1  2  1  3  1  1  1  2   -> sum = 2, sum < m이니까 rt += 1
#    lt rt
# 1  2  1  3  1  1  1  2   -> sum = 3, sum == m이니까 lt += 1(이제 sum==m이 될 일은 없으니까)
#    lt    rt
# 1  2  1  3  1  1  1  2   -> sum = 1, sum < m이니까 rt += 1
#       lt rt
# 1  2  1  3  1  1  1  2   -> sum = 4, sum > m이니까 lt += 1
#       lt    rt
# => 따라서 sum < m 이면 rt += 1 / sum >= m 이면 lt += 1

while True: # break 만날때까지 무한반복 (여기선 rt >= n 이 돼버리면 break)
    if sum < m:
        if rt < n:
            sum += list[rt] # 먼저 현재의 list[rt]를 sum에 더해주고
            rt += 1 # 그 다음 오른쪽으로 한칸
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= list[lt]
        lt += 1
    else: # sum > m 인 경우
        sum -= list[lt]
        lt += 1

print(cnt)
