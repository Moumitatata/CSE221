import heapq
import sys

def dijkstra(adj, start, target, n):
    dist = [float("inf")] * n
    parent = [-1] * n
    dist[start - 1] = 0

    pq = [(0, start)]  # (distance, node)
    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u - 1]:
            continue
        for nxt, w in adj[u - 1]:
            if dist[nxt - 1] > cur_dist + w:
                dist[nxt - 1] = cur_dist + w
                parent[nxt - 1] = u
                heapq.heappush(pq, (dist[nxt - 1], nxt))

    if dist[target - 1] == float("inf"):
        return -1, []

    # reconstruct path
    path = []
    node = target
    while node != -1:
        path.append(node)
        node = parent[node - 1]
    path.reverse()
    return dist[target - 1], path


def solve():
    input = sys.stdin.readline
    T = int(input())  # number of test cases

    for _ in range(T):
        n, m, s, d = map(int, input().split())

        u_list = list(map(int, input().split()))
        v_list = list(map(int, input().split()))
        w_list = list(map(int, input().split()))

        # build adjacency list
        adj = [[] for _ in range(n)]
        for i in range(m):
            adj[u_list[i] - 1].append((v_list[i], w_list[i]))

        distance, path = dijkstra(adj, s, d, n)

        if distance == -1:
            print(-1)
        else:
            print(distance)
            print(*path)
solve()

