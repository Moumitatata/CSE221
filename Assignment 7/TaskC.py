import heapq
import sys

def solve():
    input = sys.stdin.readline
    t = int(input())  # number of test cases

    for _ in range(t):
        n, m = map(int, input().split())

        g = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            g[u-1].append((v-1, w))
            g[v-1].append((u-1, w))  # undirected

        d = [float('inf')] * n
        d[0] = 0  # start city

        h = [(0, 0)]  # (danger, node)

        while h:
            c, u = heapq.heappop(h)
            if c > d[u]:
                continue
            for v, w in g[u]:
                nd = max(c, w)
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(h, (nd, v))

        res = [x if x != float('inf') else -1 for x in d]
        print(*res)

solve()

