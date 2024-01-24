N = int(input())
arr = [] # 리스트
arr_sum = [] #리스트 합계

for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(N):
    tmp_row = 0
    tmp_col = 0
    for j in range(N):
        tmp_row += arr[i][j] # 각 행의 합
        tmp_col += arr[j][i] # 각 열의 합
    arr_sum.append(tmp_row)
    arr_sum.append(tmp_col)

tmp1 = 0
tmp2 = 0

for i in range(N):
    tmp1 += arr[i][i] # 대각선1
    tmp2 += arr[-i][-i] # 대각선2

arr_sum.append(tmp1)
arr_sum.append(tmp2)

print(max(arr_sum))


