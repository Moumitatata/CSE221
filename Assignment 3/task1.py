def merge(l, r):
    res = []
    i = j = inv = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
            inv += len(l) - i

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1

    return res, inv

def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, x = mergesort(arr[:mid])
    right, y = mergesort(arr[mid:])
    merged, z = merge(left, right)
    total_inv = x+y+z

    return merged, total_inv 

n = int(input())
a = list(map(int, input().split()))


sorted_a, inv = mergesort(a)


print(inv)
print(*sorted_a)


    
