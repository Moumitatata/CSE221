import heapq
import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))

    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v, w = u_list[i]-1, v_list[i]-1, w_list[i]
        adj[u].append((v, w))

    INF = float('inf')
    dist = [[INF, INF] for _ in range(n)]
    dist[0][0] = 0
    dist[0][1] = 0

    heap = [(0, 0, 0), (0, 0, 1)]  # (distance, node, last_parity)

    while heap:
        d, u, lp = heapq.heappop(heap)
        if d > dist[u][lp]:
            continue
        for v, w in adj[u]:
            ep = w % 2
            if ep != lp:  # must alternate parity
                nd = d + w
                if nd < dist[v][ep]:
                    dist[v][ep] = nd
                    heapq.heappush(heap, (nd, v, ep))

    res = min(dist[n-1][0], dist[n-1][1])
    print(res if res != INF else -1)

solve()
