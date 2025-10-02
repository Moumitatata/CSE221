n,m = map(int,input().split())
u = list(map(int,input().split()))
v = list(map(int,input().split()))

in_deg = [0]*(n+1)
out_deg = [0]*(n+1)

for i in range(m):
    out_deg[u[i]]+=1
    in_deg [v[i]]+=1
result = []
for i in range(1,n+1):
    result.append(in_deg[i] - out_deg[i])

print(*result)


