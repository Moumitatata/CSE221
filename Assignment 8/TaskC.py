import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

def mst_cost_and_edges(n, edges, banned=-1, forced=-1):
    uf = UnionFind(n)
    cost, used = 0, 0
    chosen = []

    if forced != -1:
        u, v, w = edges[forced]
        if uf.union(u, v):
            cost += w
            used += 1
            chosen.append(forced)

    for i, (u, v, w) in enumerate(edges):
        if i == banned or i == forced:
            continue
        if uf.union(u, v):
            cost += w
            used += 1
            chosen.append(i)
            if used == n - 1:
                break

    return (cost, used, chosen)

def second_best_mst(n, edges):
    edges = sorted(edges, key=lambda x: x[2])

    base_cost, used, chosen = mst_cost_and_edges(n, edges)
    if used < n - 1:
        return -1 
    best = base_cost
    ans = float("inf")

    for e in chosen:
        cost, cnt, _ = mst_cost_and_edges(n, edges, banned=e)
        if cnt == n - 1 and cost > best:
            ans = min(ans, cost)

    chosen_set = set(chosen)
    for i in range(len(edges)):
        if i in chosen_set:
            continue
        cost, cnt, _ = mst_cost_and_edges(n, edges, forced=i)
        if cnt == n - 1 and cost > best:
            ans = min(ans, cost)

    return -1 if ans == float("inf") else ans

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

print(second_best_mst(N, edges))

