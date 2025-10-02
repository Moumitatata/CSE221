new = list(map(int,input().split()))
target = new[1]
len = new[0]
arr = list(map(int,input().split()))

l = 0 
r = len - 1
while l < r: 

    if arr[l] + arr[r] == target:
        print(f"{l+1} {r+1}")
        break
    elif arr[l] + arr[r] > target:
        r -= 1 
    else:
        l+=1
else:
    print("-1")
