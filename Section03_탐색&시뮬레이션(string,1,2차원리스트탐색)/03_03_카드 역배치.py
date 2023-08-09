'''
카드 역배치

1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있다. 
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.

      1 2 3 4 5 6 7 8 9 10  ...  20
카드 | 1 2 3 4 5 6 7 8 9 10  ...  20

이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다: 
구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면, 
위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다. 
이제 전체 카드가 놓인 순서는 아래 그림과 같다.

      1 2 3 4  5 6 7 8 9 10 ...  20
카드 | 1 2 3 4 10 9 8 7 6 5  ...  20

이 상태에서 구간 [9, 13]이 다시 주어진다면, 위치 9부터 위치 13까지의 카드 6, 5, 11, 12, 13을 역순으로 하여 13, 12, 11, 5, 6으로 놓는다. 
이제 전체 카드가 놓인 순서는 아래 그림과 같다.

      1 2 3 4  5 6 7 8  9 10 11 12 13 14 15  ...  20
카드 | 1 2 3 4 10 9 8 7 13 12 11 5  6  14 15  ...  20

오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치를 구하는 프로그램을 작성하시오.

▣ 입력설명
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 
이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.

▣ 출력설명
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.

▣ 입력예제 1 
5 10
9 13
1 2
3 4 
5 6 
1 2 
3 4 
5 6 
1 20 
1 20

▣ 출력예제 1
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''

cards = list(range(21)) # 이 방법 기억!⭐️

for _ in range(10): # _ 사용시 변수 없이 반복문만 돎
    a, b = map(int, input().split())
    for j in range((b-a+1)//2):
        # 나의풀이 -> 이 풀이도 맞긴 한데 더 쉬운 풀이가 밑에 있음!
        # tmp = cards[a+j]
        # cards[a+j] = cards[b-j]
        # cards[b-j] = tmp

        # 강의풀이 -> 두 변수의 값을 바꿀 때 사용하면 엄청편함!⭐️
        cards[a+j], cards[b-j] = cards[b-j], cards[a+j]
        
    print(cards)

cards.pop(0) # 0번째 인덱스 삭제

for x in cards:
    print(x, end=' ')