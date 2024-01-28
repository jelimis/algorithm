arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

for i in range(9):
    ch1 = [0] * 9
    ch2 = [0] * 9
    for j in range(9):
        ch1[arr[i][j]-1] = 1
        ch2[arr[j][i]-1] = 1
    if sum(ch1) != 9 or sum(ch2) != 9:
        print("NO")
        break

for i in range(3):
    for j in range(3):
        ch3 = [0] * 10
        for k in range(3):
            for s in range(3):
                ch3[arr[i*3+k][j*3+s]-1] = 1
        if sum(ch3) != 9:
            print("NO")
            break







