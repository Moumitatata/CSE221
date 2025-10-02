from collections import deque
def solve():
    N=int(input())
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        print(0)
        return
        
    dist = [[-1] * (N+1) for _ in range(N+1)]
    directions = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    
    q = deque()
    dist[x1][y1] = 0
    q.append((x1, y1))
    
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            print(dist[x][y])
            return
            
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= N and 1 <= ny <= N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
    print(-1)

solve()