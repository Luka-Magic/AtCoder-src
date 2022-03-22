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
    for a, b in combinations(li, 2):
        pmax = a + b
        ans += bisect.bisect_left(li, pmax) - bisect.bisect_right(li, b)
    print(ans)

if __name__ == '__main__':
    main()