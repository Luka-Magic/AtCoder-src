import sys
sys.setrecursionlimit(10 ** 6)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    masu = [list(map(int, input().split())) for _ in range(h)]
    
    seen = [[-1] * w for _ in range(h)]
    
    def dfs(x, y, i):
        if seen[y][x] != -1:
            return
        seen[y][x] = i
        for px, py in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
            nx = x + px
            ny = y + py
            if nx >= 0 and nx < w and ny >= 0 and ny < h and masu[ny][nx] == 1 and seen[ny][nx] == -1:
                dfs(nx, ny, i)
    i = 0
    for y in range(h):
        for x in range(w):
            if masu[y][x] == 1 and seen[y][x] == -1:
                i += 1
                dfs(x, y, i)
    ans = 0
    for y in range(h):
        for x in range(w):
            ans = max(ans, seen[y][x])
    print(ans)