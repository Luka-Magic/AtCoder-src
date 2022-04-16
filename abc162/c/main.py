import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    import math
    from functools import reduce
    def gcd(*numbers):
        return reduce(math.gcd, numbers)
    ans = 0
    k = int(input())
    from itertools import product
    for a, b, c in product(list(range(1, k+1)), repeat=3):
        ans += gcd(a, b, c)
    print(ans)

if __name__ == '__main__':
    main()
