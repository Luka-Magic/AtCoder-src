from itertools import accumulate
import bisect
import sys
from itertools import combinations

input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    from collections import Counter
    c = Counter(li)
    c = [c[i] if i in c else 0 for i in range(max(li)+1)]
    s = list(accumulate(c))
    s_max = len(s)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = li[i], li[j]
            left, right = abs(a - b) + 1, min(a + b - 1, s_max - 1)
            ans += s[right] - s[left - 1]
            ans -= 1 if left <= a <= right else 0
            ans -= 1 if left <= b <= right else 0
    print(ans // 6)

if __name__ == '__main__':
    main()
