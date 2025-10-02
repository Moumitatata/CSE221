def binary_tree(arr, l, r, res):
    if l > r:
        return
    mid = (l + r) // 2
    res.append(arr[mid])
    binary_tree(arr, l, mid - 1, res)
    binary_tree(arr, mid + 1, r, res)
n = int(input())
arr = list(map(int, input().split()))
res = []
binary_tree(arr, 0, n - 1, res)
print(*res)