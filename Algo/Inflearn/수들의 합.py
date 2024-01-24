N, M = map(int, input().split())
arr = list(map(int, input().split()))

lt, rt, = 0, 1
tot = arr[0]
cnt = 0 # 개수

while True:
    if tot < M:
        if rt < N:
            tot += arr[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt +=1
        tot -= arr[lt]
        lt +=1
    else:
        tot -= arr[lt] # M보다 크면 넘긴다.
        lt +=1
print(cnt)
