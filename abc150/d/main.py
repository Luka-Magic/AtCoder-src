import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

import math
from functools import reduce
def lcm(*numbers):
    def lcm_base(x, y):
        return (x * y) // math.gcd(x, y)
    return reduce(lcm_base, numbers, 1)

def main():
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    p = []
    a0 = li[0]
    c = 0
    while a0 % 2 == 0:
        c += 1
        a0 //= 2
    for a in li:
        if (a % (2**c) == 0) and ((a // 2) % (2**c) != 0):
            p.append(a // 2)
        else:
            print(0)
            exit()
    k = lcm(*p)
    print((m - k) // (2*k) + 1)

if __name__ == '__main__':
    main()