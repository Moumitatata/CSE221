x = int(input())
arr = list(map(int, input().split()))
swapped = True

while swapped:
    swapped = False
    for i in range(x - 1):
        if arr[i] > arr[i + 1] and (arr[i] % 2) == (arr[i + 1] % 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

print(' '.join(map(str, arr)))