from collections import deque

import sys
sys.setrecursionlimit(2*100000+5)

def bfs(start, n, graph):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    farthest_node = start
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v
    return farthest_node, dist[farthest_node]

def solve():
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    node_a, _ = bfs(1, n, graph)
    node_b, diameter = bfs(node_a, n, graph)

    print(diameter)
    print(node_a, node_b)

solve()