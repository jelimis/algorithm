N = int(input()) # 항상 홀수
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0 # 결과값
v = N//2 # 행렬의 중간 기준값

for i in range(v):
    for j in range(N):
        if (v-i) <= j <= (v+i):
            cnt += arr[i][j]
            cnt += arr[-i+N-1][j] # 다이아몬드라 반대편도 같은 모양
cnt += sum(arr[N//2]) # 중간 행렬 값

print(cnt)
