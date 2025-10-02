N, M, K = map(int, input().split())

arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split()))

left = 0
right = M-1

result1 = [-1 , -1]
result = []

closest_diff = float("inf")

while left < N and right >= 0:

    if arr1[left] + arr2[right] == K :
        result.append(left+1)
        result.append(right+1)
        break
    
    elif abs(K - (arr1[left] + arr2[right])) < closest_diff :
        closest_diff = abs(K - (arr1[left] + arr2[right]))
        result1 = [left+1 , right+1]

    if arr1[left] + arr2[right] < K :
        left += 1
    else:
        right -= 1

for i in (result if result else result1):
    print(i, end=" ")
