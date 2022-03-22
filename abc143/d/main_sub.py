import bisect
import sys

input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    from itertools import combinations
    ans = 0
    for i in combinations(li, 2):
        a, b = max(i), min(i)
        pmin = a - b
        pmax = a + b
        k = 0
        if pmin < a < pmax:
            k -= 1
        if pmin < b < pmax:
            k -= 1
        s = bisect.bisect_right(li, pmin)
        t = bisect.bisect_left(li, pmax)
        k += t - s
        ans += k
    print(ans // 3)
if __name__ == '__main__':
    main()