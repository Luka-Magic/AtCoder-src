import sys
input = sys.stdin.readline
from collections import deque

mod = 10**9 + 7
inf = float('inf')


def main():
    w, h = map(int, input().split())
    masu = [list(map(int, input().split())) for _ in range(h)]
    # 1に囲まれている0を1に変えちゃう。
    seen = [[-1] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            z_li = []
            if masu[y][x] == 0 and seen[y][x] == -1 and 0 < x < w-1 and 0 < y < h-1:
                que = deque([(x, y)])
                seen[y][x] = 1
                z_li.append((x, y))
                flag = True
                while que:
                    x_, y_ = que.popleft()
                    # print(x_ + 1, y_ + 1)
                    if y_ % 2 == 0:
                        dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1)]
                    else:
                        dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (-1, -1), (-1, 1)]
                    for px, py in dires:
                        nx = x_ + px
                        ny = y_ + py
                        if 0 <= nx < w and 0 <= ny < h and masu[ny][nx] == 0 and seen[ny][nx] == -1:
                            if 0 < nx < w - 1 and 0 < ny < h - 1:
                                seen[ny][nx] = 1
                                z_li.append((nx, ny))
                                que.append((nx, ny))
                            elif nx == 0 or nx == w-1 or ny == 0 or ny == h-1:
                                # print(nx+1, ny+1)
                                seen[ny][nx] = 1
                                z_li.append((nx, ny))
                                que.append((nx, ny))
                                flag = False
                if flag:
                    for ax, ay in z_li:
                        masu[ay][ax] = 1
    
    # 1の周りの飾りの長さ求める
    ans = 0
    y, x, y_, x_ = 0, 0, 0, 0
    seen = [[-1] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if masu[y][x] == 1 and seen[y][x] == -1:
                seen[y][x] = 1
                que = deque([(x, y)])
                while que:
                    x_, y_ = que.popleft()
                    if y_ % 2 == 0:
                        dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1)]
                    else:
                        dires = [(1, 0), (0, -1), (-1, 0), (0, 1), (-1, -1), (-1, 1)]
                    for px, py in dires:
                        nx = x_ + px
                        ny = y_ + py
                        if 0 <= nx < w and 0 <= ny < h:
                            if masu[ny][nx] == 0:
                                ans += 1
                            else:
                                if seen[ny][nx] == -1:
                                    seen[ny][nx] = 1
                                    que.append((nx, ny))
                        else:
                            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
