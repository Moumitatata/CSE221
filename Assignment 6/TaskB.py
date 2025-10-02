from collections import deque

def solve():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    visited = [0] * (n + 1)  
    ans = 0

    for i in range(1, n + 1):
        if visited[i] == 0:     
            q = deque([i])
            visited[i] = 1
            count1, count2 = 1, 0

            while q:
                u = q.popleft()
                for v in g[u]:
                    if visited[v] == 0:
                        visited[v] = -visited[u]  
                        if visited[v] == 1:
                            count1 += 1
                        else:
                            count2 += 1
                        q.append(v)

            ans += max(count1, count2)

    print(ans)
solve()