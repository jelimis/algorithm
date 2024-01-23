numbers = [i+1 for i in range(20)]
for i in range(10):
    start, end = map(int, input().split())
    tmp = numbers[start-1:end]
    tmp = tmp[::-1]
    for j in range(len(tmp)):
        numbers[j+start-1] = tmp[j]

for n in numbers:
    print(n, end=' ')