import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def f(a, b):
    return (((b+a) * (b-a+1)) // 2) % mod


def main():
    a, b = map(int, input().split())
    s = len(str(a))
    e = len(str(b))
    if s == e:
        print(s * f(a, b) % mod)
        exit()

    ans = 0
    for i in range(s, e+1):
        x = max(a, 10**(i-1))
        y = min(b, 10**i -1)
        ans += i * f(x, y) % mod

    print(ans % mod)


if __name__ == '__main__':
    main()
