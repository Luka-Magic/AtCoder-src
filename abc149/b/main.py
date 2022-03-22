import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, k = map(int, input().split())
    s = max(a-k, 0)
    t = max(b-max((k-a), 0), 0)
    print(s, t)


if __name__ == '__main__':
    main()
