#Is Sorted?
x = int(input())
for i in range (x):
    m = int(input())
    arr = list(map(int,input().split(' ')))
    flag = True 
    for k in range(m-1):
        if arr[k] <= arr[k+1]:
            continue 
        else:
            flag = False

    if flag:
        print("YES")
    else:
        print("NO")
