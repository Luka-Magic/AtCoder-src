mod = 10**9 + 7
inf = float('inf')

def main():
    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    masu = [list(input()) for _ in range(h)]
    sy, sx = sy-1, sx-1
    gy, gx = gy-1, gx-1

    from collections import deque

    def bfs():
        seen = [[float('inf')]*w for _ in range(h)]
        que = deque([])
        que2 = deque([])
        que.append((sx,sy))
        que2.append((sx, sy))
        seen[sy][sx] = 0
        while que:
            while que:
                a,b = que.popleft()
                if a==gx and b == gy:
                    break
                for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nx = a+x
                    ny = b+y
                    if 0<=nx<w and 0<=ny<h and masu[ny][nx] != '#' and seen[ny][nx] == float('inf'):
                        seen[ny][nx] = min(seen[b][a], seen[ny][nx])
                        que.append((nx,ny))
                        que2.append((nx,ny))
            if seen[gy][gx] != inf:
                break
            while que2:
                a, b = que2.popleft()
                for wx in range(-2, 3):
                    for wy in range(-2, 3):
                        nx = a+wx
                        ny = b+wy
                        if 0 <= nx < w and 0 <= ny < h and masu[ny][nx] != '#' and seen[ny][nx] == float('inf'):
                            seen[ny][nx] = min(seen[b][a]+1, seen[ny][nx])
                            que.append((nx, ny))
        return seen

    seen = bfs()
    ans = seen[gy][gx]
    print(ans if ans != inf else -1)

if __name__ == '__main__':
    main()
