import sys
input = sys.stdin.readline

def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b, parent, rank):
    ra = find(a, parent)
    rb = find(b, parent)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()  

    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)

    total_cost = 0
    for w, u, v in edges:
        if union(u, v, parent, rank):
            total_cost += w

    print(total_cost)

if __name__ == "__main__":
    solve()
