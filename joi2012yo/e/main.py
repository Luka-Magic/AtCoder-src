import sys
input = sys.stdin.readline
from collections import deque

mod = 10**9 + 7
inf = float('inf')


def main():
    w, h = map(int, input().split())
    masu = [[0] * (w+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(h)] + [[0] * (w+2)]
    
    ans = 0
    seen = [[0] * (w+2) for _ in range(h+2)]
    que = deque([(0, 0)])
    seen[0][0] = 1
    while que:
        x, y = que.popleft()
        if y % 2 == 0:
            dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (-1, 1), (-1, -1)]
        else:
            dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1)]
        for px, py in dires:
            nx = x + px
            ny = y + py
            if 0 <= nx < w+2 and 0 <= ny < h+2 and seen[ny][nx] == 0:
                if masu[ny][nx] == 0:
                    seen[ny][nx] = 1
                    que.append((nx, ny))
                elif masu[ny][nx] == 1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
