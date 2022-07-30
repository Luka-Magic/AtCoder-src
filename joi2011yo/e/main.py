from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    h, w, n = map(int, input().split())
    masu = [list(input()) for _ in range(h)]

    ch_dic = {}

    for y in range(h):
        for x in range(w):
            if masu[y][x] not in ['X', '.', 'S']:
                su = masu[y][x]
                ch_dic[su] = (x, y)
            if masu[y][x] == 'S':
                start = (x, y)

    ans = 0
    sx, sy = start
    for i in range(n):
        gx, gy = ch_dic[str(i+1)]
        seen = [[-1] * w for _ in range(h)]
        seen[sy][sx] = 0
        que = deque([(sx, sy)])
        while que:
            x, y = que.popleft()
            if x == gx and y == gy:
                break
            for px, py in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx = x + px
                ny = y + py
                if nx >= 0 and nx < w and ny >= 0 and ny < h and seen[ny][nx] == -1 and masu[ny][nx] != 'X':
                    seen[ny][nx] = seen[y][x] + 1
                    que.append((nx, ny))
        ans += seen[gy][gx]
        sx, sy = gx, gy
    print(ans)

if __name__ == '__main__':
    main()