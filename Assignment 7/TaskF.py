import heapq
def second_shortest(n, m, s, d, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u-1].append((v-1, w))
        adj[v-1].append((u-1, w))

    dist = [[float("inf")] * 2 for _ in range(n)]
    dist[s-1][0] = 0

    pq = [(0, s-1)]  

    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u][1]:
            continue
        for v, w in adj[u]:
            new = cost + w

            if new < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new
                heapq.heappush(pq, (new, v))

            elif dist[v][0] < new < dist[v][1]:
                dist[v][1] = new
                heapq.heappush(pq, (new, v))

    return -1 if dist[d-1][1] == float("inf") else dist[d-1][1]


def solve():
    n, m, s, d = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(second_shortest(n, m, s, d, edges))


solve()
