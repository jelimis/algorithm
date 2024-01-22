numbers = list(map(int, input().split()))

check_as = True
check_ds = True

for i in range(1, len(numbers)):
    if numbers[i - 1] > numbers[i]:
        check_as = False
    if numbers[i - 1] < numbers[i]:
        check_ds = False

if check_as:
    print('ascending')
elif check_ds:
    print('descending')
else:
    print('mixed')