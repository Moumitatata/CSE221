nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes + 1)]

for i in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)

status = [0] * (nodes + 1)
cycle_found = 0

for u in range(1, nodes + 1):
    if status[u] != 0:
        continue
    stack = [(u, 0)]
    status[u] = 1
    while stack:
        current, child_index = stack[-1]
        if child_index < len(graph[current]):
            neighbor = graph[current][child_index]
            stack[-1] = (current, child_index + 1)
            if status[neighbor] == 0:
                status[neighbor] = 1
                stack.append((neighbor, 0))
            elif status[neighbor] == 1:
                cycle_found = 1
                stack = []
                break
        else:
            status[current] = 2
            stack.pop()

print("YES" if cycle_found else "NO")

