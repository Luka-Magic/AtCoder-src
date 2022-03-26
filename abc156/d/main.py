import sys
input = sys.stdin.readline
import math

mod = 10**9 + 7


def pow_(x, n, mod):
    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n >>= 1
    return ans

def cmb(n, k):
    res = 1
    for i in range(k):
        res *= (n - i)
        res %= mod
    for j in range(1, k+1):
        res *= pow(j, mod-2, mod)
        res %= mod
    return res % mod

def main():
    n, a, b = map(int, input().split())
    k = pow_(2, n , mod) - 1

    print((k - cmb(n, a) - cmb(n, b)) % mod)

if __name__ == '__main__':
    main()
