# 최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 최솟값 저장하는 변수. 최초값은 파이썬에서 가장 큰 값인 float('inf')⭐️ 

for i in range(len(arr)):
    if arr[i] < arrMin: # <= 로 등호가 붙으면 같은 값을 가진 마지막 애가 저장됨
        arrMin = arr[i]

print(arrMin)