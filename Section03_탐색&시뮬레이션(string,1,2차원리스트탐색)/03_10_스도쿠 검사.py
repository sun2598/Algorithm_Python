'''
스도쿠 검사

스도쿠는 매우 간단한 숫자 퍼즐이다. 
9x9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3x3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 
예를 들어 다음을 보자.

1 4 3 | 6 2 8 | 5 7 9 
5 7 2 | 1 3 9 | 4 6 8 
9 8 6 | 7 5 4 | 2 3 1 
---------------------
3 9 1 | 5 4 2 | 7 8 6 
4 6 8 | 9 1 7 | 3 5 2 
7 2 5 | 8 6 3 | 9 1 4 
---------------------
2 3 7 | 4 8 1 | 6 9 5 
6 1 9 | 2 7 5 | 8 4 3 
8 5 4 | 3 9 6 | 1 2 7

위 그림은 스도쿠를 정확하게 푼 경우이다. 
각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 
각 3x3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9x9 크기의 스도쿠가 주어지면 정확하게 풀었으면 “YES", 잘못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9x9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

▣ 입력예제 1 
1 4 3 6 2 8 5 7 9 
5 7 2 1 3 9 4 6 8 
9 8 6 7 5 4 2 3 1 
3 9 1 5 4 2 7 8 6 
4 6 8 9 1 7 3 5 2 
7 2 5 8 6 3 9 1 4 
2 3 7 4 8 1 6 9 5 
6 1 9 2 7 5 8 4 3 
8 5 4 3 9 6 1 2 7

▣ 출력예제 1 
YES
'''

#      1 2 3 4 5 6 7 8 9 (0번 인덱스 사용X)
# ch | 0 0 0 0 0 0 0 0 0

# -> 해당 숫자가 나타나면 그 숫자에 해당하는 인덱스 값을 1로 만듦
#      1 2 3 4 5 6 7 8 9
# ch | 1 1 1 1 1 1 1 1 1

def check(a):
    # 1. 행/열 체크
    for i in range(9):
        ch1 = [0] * 10 # 행 체크 리스트
        ch2 = [0] * 10 # 열 체크 리스트
        for j in range(9):
            ch1[a[i][j]] = 1 # 행 체크 리스트를 채워줌
            ch2[a[j][i]] = 1 # 열 체크 리스트를 채워줌
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
        
    # 2. 사각형 체크
    for i in range(3): # 0,1,2
        for j in range(3): # 0,1,2
            ch3 = [0] * 10 # 사각형 체크 리스트 (i,j for문에서 사각형 그룹 정해지는거. 9개의 그룹 생성)
            for k in range(3):
                for l in range(3):
                    ch3[a[i*3+k][j*3+l]] = 1 # 사각형 체크 리스트를 채워줌⭐️
            if sum(ch3) != 9:
                return False
            
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")


