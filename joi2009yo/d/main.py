import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

m = int(input())
n = int(input())
masu = [list(map(int, input().split())) for _ in range(n)]

ans = 0
seen = [[0] * m for _ in range(n)]

def dfs(x, y, c, seen):
    global ans
    seen[y][x] = c
    ans = max(ans, c)
    for b, a in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nx = x + a
        ny = y + b
        if nx >= 0 and nx < m and ny >= 0 and ny < n and masu[ny][nx] == 1 and seen[ny][nx] == 0:
            dfs(nx, ny, c+1, seen)
    seen[y][x] = 0

for i in range(n):
    for j in range(m):
        if masu[i][j] == 1:
            dfs(j, i, 1, seen)
                
print(ans)