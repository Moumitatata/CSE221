from queue import PriorityQueue
import sys

class G:
    def __init__(self, n):
        self.e = [[] for _ in range(n)]  # edges

    def add(self, u, v, w):
        self.e[u-1].append((v, w))

def dijkstra(g, s, n):
    d = [float('inf')] * n
    p = [None] * n
    d[s-1] = 0
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        du, u = q.get()
        if du > d[u-1]:
            continue
        for v, w in g.e[u-1]:
            if d[u-1] + w < d[v-1]:
                d[v-1] = d[u-1] + w
                p[v-1] = u
                q.put((d[v-1], v))
    return d, p

def solve():
    input = sys.stdin.readline
    t = int(input())  # number of test cases

    for _ in range(t):
        n, m, a, b = map(int, input().split())
        g = G(n)
        for _ in range(m):
            u, v, w = map(int, input().split())
            g.add(u, v, w)

        da, _ = dijkstra(g, a, n)
        db, _ = dijkstra(g, b, n)

        best_time = float('inf')
        meet = -1

        for i in range(n):
            if da[i] == float('inf') or db[i] == float('inf'):
                continue
            t = max(da[i], db[i])
            if t < best_time or (t == best_time and i+1 < meet):
                best_time = t
                meet = i+1

        if meet == -1:
            print(-1)
        else:
            print(f"{best_time} {meet}")

solve()
