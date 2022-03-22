import bisect
import sys
from itertools import combinations

input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    ans = 0
    for a in range(n):
        c = a + 2
        for b in range(a+1, n):
            while (c < n) and (li[c] < li[a] + li[b]):
                c += 1
            ans += c - b - 1
    print(ans)

if __name__ == '__main__':
    main()
