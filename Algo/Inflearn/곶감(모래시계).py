N = int(input())
arr = []
cnt = 0
for i in range(N):
    arr.append(list(map(int, input().split())))

M = int(input())

for i in range(M):
    A, B, C = map(int, input().split())
    if B == 0:
        for _ in range(C):
            arr[A-1].append(arr[A-1].pop(0))
    else:
        for _ in range(C):
            arr[A-1].insert(0, arr[A-1].pop())

s=0
e=N-1

for i in range(N):
    for j in range(s, e+1):
        cnt += arr[i][j]
    if i<N//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(cnt)