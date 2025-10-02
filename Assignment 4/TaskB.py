#TASK B
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj_lst = [[] for i in range(N + 1)]  
for i in range(M):
   adj_lst [u[i]].append((v[i], w[i]))
for i in range(1, N + 1):
    result = f"{i}:"
    if adj_lst [i]:
        result += " ".join(f"({m[0]},{m[1]})" for m in adj_lst [i])
    print(result)