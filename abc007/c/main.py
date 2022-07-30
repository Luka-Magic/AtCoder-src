import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

from collections import deque

def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    masu = [list(input()) for _ in range(r)]

    seen = [[-1] * c for _ in range(r)]
    seen[sy-1][sx-1] = 0
    que = deque([(sx-1, sy-1)])

    while que:
        x, y = que.popleft()
        if x == gx - 1 and y == gy - 1:
            break
        for px, py in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx = x + px
            ny = y + py
            if nx >= 0 and nx < c and ny >= 0 and ny < r and seen[ny][nx] == -1 and masu[ny][nx] != '#':
                seen[ny][nx] = seen[y][x] + 1
                que.append((nx, ny))
    
    print(seen[gy - 1][gx - 1])
    




if __name__ == '__main__':
    main()
