import copy
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    x_, y_ = map(int, input().split())
    masu = [[float('inf')] * (x_+1) for _ in range((y_+1))]
    new_masu = [[float('inf')] * (x_+1) for _ in range((y_+1))]

    for _ in range(n):
        a, b = map(int, input().split())
        for x in range(x_+1):
            for y in range(y_+1):
                if masu[y][x] != float('inf'):
                    xa, yb = min(x_, x+a), min(y_, y+b)
                    new_masu[yb][xa] = min(new_masu[yb][xa], masu[y][x] + 1)
        a, b = min(a, x_), min(b, y_)
        new_masu[b][a] = 1
        masu = [i[:] for i in new_masu]

    ans = float('inf')
    for i in range(x, x_+1):
        for j in range(y, y_+1):
            ans = min(ans, masu[j][i])
    if ans == float('inf'):
        ans = -1
    print(ans)


if __name__ == '__main__':
    main()
