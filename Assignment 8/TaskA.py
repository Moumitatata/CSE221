import sys
sys.setrecursionlimit(10**7)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)  # path compression
    return parent[x]

def union(a, b, parent, size):
    rootA = find(a, parent)
    rootB = find(b, parent)
    if rootA != rootB:

        if size[rootA] < size[rootB]:
            rootA, rootB = rootB, rootA
        parent[rootB] = rootA
        size[rootA] += size[rootB]
    return size[find(rootA, parent)]

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    parent = [i for i in range(N+1)]
    size = [1] * (N+1)

    for i in range(K):
        a, b = map(int, input().split())
        print(union(a, b, parent, size))
solve()