from operator import mul
from functools import reduce
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    n, k = map(int, input().split())
    for i in range(1, k+1):
        if n-k < i-1:
            print(0)
        else:
            print(cmb(k-1, i-1) * cmb(n-k+1, i) % mod)


if __name__ == '__main__':
    main()
