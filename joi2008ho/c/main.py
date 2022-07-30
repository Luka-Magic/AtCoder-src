import sys
input = sys.stdin.readline
import bisect

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = []
    for _ in range(n):
        li.append(int(input()))
    li.append(0)
    li2 = []
    for i in li:
        for j in li:
            li2.append(i + j)
    li2.sort()
    ans = 0
    l2 = len(li2)
    for j in li2:
        f = m - j
        if f < 0:
            continue
        i = bisect.bisect_right(li2, f) - 1
        # i = min(i, l2-1)
        v = li2[i]
        if j + v > m:
            continue
        ans = max(ans, j + v)
    print(ans)

if __name__ == '__main__':
    main()
