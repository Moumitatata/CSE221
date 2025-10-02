def has_eulerian(n,m,u,v):
    deg = [0]*(n+1)
    for i in range(m):
        deg[u[i]]+=1
        deg[v[i]]+=1

    odd_count = sum(1 for i in deg[1:] if i%2!=0 )  #so basically its giving 1 everytime so 1+1+..
    return "YES" if odd_count == 0 or odd_count==2 else 'NO'

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
print(has_eulerian(n, m, u, v))
    