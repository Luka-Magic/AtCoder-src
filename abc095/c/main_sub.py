import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c, x, y = map(int, input().split())
    ans = inf
    for i in range(max(x, y) + 1):
        p = a * max(x - i, 0) + b * max(y - i, 0) + c * 2 * i
        ans = min(ans, p)
    print(ans)

if __name__ == '__main__':
    main()
