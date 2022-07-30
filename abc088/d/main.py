import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    h, w = map(int, input().split())
    masu = [list(input()) for _ in range(h)]

    seen = [[-1] * w for _ in range(h)]
    seen[0][0] = 1
    from collections import deque
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        if x == w-1 and y == h-1:
            break
        for px, py in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx = x + px
            ny = y + py
            if 0 <= nx < w and 0 <= ny < h and seen[ny][nx] == -1 and masu[ny][nx] != '#':
                seen[ny][nx] = seen[y][x] + 1
                que.append((nx, ny))

    wall_count = 0
    for y in range(h):
        for x in range(w):
            if masu[y][x] == '#':
                wall_count += 1
    if seen[-1][-1] == -1:
        print(-1)
        exit()
    print(h * w - wall_count - seen[-1][-1])

if __name__ == '__main__':
    main()
