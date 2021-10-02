import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def g1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)


def g2(x):
    x = list(str(x))
    x.sort()
    x = ''.join(x)
    return int(x)


def f(x):
    return g1(x) - g2(x)


def main():
    n, k = map(int, input().split())
    for _ in range(k):
        n = f(n)
    print(n)


if __name__ == '__main__':
    main()
