length, query = map(int, input().split())
arr = list(map(int, input().split()))

def LeftSide(arr,target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right )//2        
        
        if arr[mid] < target :
            left = mid + 1 
        else:
            right = mid

    return left

def RightSide(arr,target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right )//2        
        
        if arr[mid] <= target :
            left = mid + 1 
        else:
            right = mid

    return left

for i in range(query):
    x,y = map(int, input().split())
    
    left = LeftSide(arr,x)
    right = RightSide(arr,y)

    print(right - left)