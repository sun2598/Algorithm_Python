'''
두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제 1 
3
1 3 5
5
2 3 6 7 9

▣ 출력예제 1 
1 2 3 3 5 6 7 9
'''

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

# 나의방법 -> 좀 더 느림!
# list = list1 + list2
# list.sort() # sort() 사용시 8log8의 시간복잡도

# 강의방법 -> 좀 더 빠름!
# <two pointer algorithm>
#         p1
# list1 : 1  3  5           // list1[p1] < list2[p2] 인지 비교
# list2 : 2  3  5  7  9     //  -> 맞으면 list1[p1]을 list에 더해주고, p1 += 1
#         p2
p1 = p2 = 0
list = []
while p1 < n and p2 < m: # 둘 중 하나라도 끝까지 가면 while문 중단
    if list1[p1] <= list2[p2]:
        list.append(list1[p1])
        p1 += 1
    else:
        list.append(list2[p2])
        p2 += 1
# 남은 것들 처리
if p1 < n: # p2가 끝나서 p1이 남아있는 경우
    list = list + list1[p1:]
if p2 < m: # p1이 끝나서 p2가 남아있는 경우
    list = list + list2[p2:]

for x in list:
    print(x, end=' ')