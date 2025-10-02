import math
nodes, queries = map(int, input().split())
adjacency = [[] for _ in range(nodes + 1)]

for a in range(1, nodes + 1):
    for b in range(1, nodes + 1):
        if a != b and math.gcd(a, b) == 1:
            adjacency[a].append(b)

for i in range(queries):
    node, k = map(int, input().split())
    if len(adjacency[node]) >= k:
        print(adjacency[node][k - 1])
    else:
        print("-1")
