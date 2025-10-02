# Input number of nodes and root
n, root = map(int, input().split())

# Build adjacency list (graph representation)
graph = {}
for i in range(1, n + 1):
    graph[i] = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Array to store subtree sizes
subtree_size = [0] * (n + 1)

# Iterative DFS using a stack
stack = [(root, 0, 0)]  
# (current_node, parent_node, state)
# state = 0 → process children later
# state = 1 → all children processed, compute size

while stack:
    node, parent, state = stack.pop()
    if state == 0:
        # Push current node back with state=1 (post-processing)
        stack.append((node, parent, 1))
        # Push all children
        for neighbor in graph[node]:
            if neighbor != parent:
                stack.append((neighbor, node, 0))
    else:
        # Now compute the subtree size
        size = 1  # count itself
        for neighbor in graph[node]:
            if neighbor != parent:
                size += subtree_size[neighbor]
        subtree_size[node] = size

# Queries
q = int(input())
for _ in range(q):
    query_node = int(input())
    print(subtree_size[query_node])
'''graph = {
  1: [3,2],
  2: [1,4],
  3: [1],
  4: [2]
}'''