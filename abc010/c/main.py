import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    sx, sy, gx, gy, t, v = map(int, input().split())
    n = int(input())
    m = t * v
    for _ in range(n):
        x, y = map(int, input().split())
        d = math.sqrt((x - sx)**2 + (y - sy)**2) + \
            math.sqrt((x - gx)**2 + (y - gy)**2)
        # print(d)
        if m >= d:
            print('YES')
            exit()
    print('NO')


if __name__ == '__main__':
    main()
