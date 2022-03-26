from collections import deque

mod = 10**9 + 7
inf = float('inf')


def main():
    h, w = map(int, input().split())
    masu = [list(input()) for _ in range(h)]

    def bfs(sx, sy):
        seen = [[float('inf')]*w for _ in range(h)]
        que = deque([])
        que.append((sx, sy))
        seen[sy][sx] = 0
        max_step = 0
        while que:
            a, b = que.popleft()
            max_step = max(max_step, seen[b][a])
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = a+x
                ny = b+y
                if 0 <= nx < w and 0 <= ny < h:
                    if masu[ny][nx] != '#' and seen[ny][nx] == float('inf'):
                        seen[ny][nx] = seen[b][a] + 1
                        que.append((nx, ny))
        return max_step

    ans = 0
    for sy in range(h):
        for sx in range(w):
            if masu[sy][sx] == '#':
                continue
            ans = max(ans, bfs(sx, sy))
    print(ans)


if __name__ == '__main__':
    main()
