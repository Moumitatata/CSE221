N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
max_len = 0
total = 0

for i in range(N):
    total+= arr[i]
    
    while total > K:
        total-= arr[left]
        left += 1

    max_len = max(max_len, i - left + 1)

print(max_len)


