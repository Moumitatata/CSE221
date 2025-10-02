# Reverse Sorting
def count_inversions(arr):
    count = 0
    x = len(arr)
    for i in range(x):
        for j in range(i + 1, x):
            if arr[i] > arr[j]:
                count += 1
    return count

# Input reading
X = int(input())
arr = list(map(int, input().split()))

# Arrays with fewer than 3 elements can always be sorted
if X == 1:
    print("YES")
elif X == 2:
    if arr[0] <= arr[1]:
        print("YES")
    else:
        print("NO")
else:
    inversions = count_inversions(arr)
    if inversions % 2 == 0:
        print("YES")
    else:
        print("NO")
