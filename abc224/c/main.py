import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    from itertools import combinations
    ans = 0
    for i in combinations(li, 3):
        a, b, c = i[0], i[1], i[2]
        dx1 = b[0] - a[0]
        dx2 = c[0] - a[0]
        dy1 = b[1] - a[1]
        dy2 = c[1] - a[1]
        if dx2 * dy1 == dx1 * dy2:
            continue
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
