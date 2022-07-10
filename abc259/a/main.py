import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m, x, t, d = map(int, input().split())
    if m >= x:
        print(t)
    else:
        print(t - (x - m) * d)


if __name__ == '__main__':
    main()
