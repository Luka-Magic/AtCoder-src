from functools import reduce
import math
import sys
input = sys.stdin.readline

def gcd(*numbers):
      return reduce(math.gcd, numbers)
mod = 10**9 + 7
inf = float('inf')


def main():
    n, a, b = map(int, input().split())
    ans = n * (n+1) // 2
    p =  n // a
    ans -= (p * (p+1) // 2) * a
    q = n // b
    ans -= (q * (q+1) // 2) * b
    g = a * b // gcd(a, b)
    r = n // g
    ans += (r * (r+1) // 2) * g
    print(ans)


if __name__ == '__main__':
    main()
