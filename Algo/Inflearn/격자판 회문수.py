arr = []

for i in range(7):
    arr.append(list(map(int, input().split())))

cnt = 0

for i in range(7):
    for j in range(3):
        check1 = True
        check2 = True
        for k in range(2):
            if arr[i][j+k] != arr[i][4+j-k]:
                check1 = False
            if arr[j+k][i] != arr[4+j-k][i]:
                check2 = False
        if check1 or check2:
            cnt += 1

print(cnt)



