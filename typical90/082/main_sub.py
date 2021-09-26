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
        if i == s:
            ans += i * f(a, 10**s-1) % mod
        elif i == e:
            ans += i * f(10**(e-1), b) % mod
        else:
            ans += i * f(10**(i-1), 10**i - 1) % mod

    print(ans % mod)


if __name__ == '__main__':
    main()
