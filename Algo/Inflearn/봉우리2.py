N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [-1,0,1,0]

arr.insert(0, [0]*N)
arr.append([0]*N)
for x in arr:
    x.insert(0,0)
    x.append(0)
cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)