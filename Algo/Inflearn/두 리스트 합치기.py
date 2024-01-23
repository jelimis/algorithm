first = int(input())
arr1 = list(map(int, input().split()))

second = int(input())
arr2 = list(map(int, input().split()))

result = arr1 + arr2
result.sort()
print(result)