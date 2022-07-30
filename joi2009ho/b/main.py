import sys
input = sys.stdin.readline

import bisect

mod = 10**9 + 7
inf = float('inf')


def main():
    D = int(input())
    N = int(input())
    M = int(input())
    d_li = [int(input()) for _ in range(N-1)]
    k_li = [int(input()) for _ in range(M)]

    d_li.append(0)
    d_li.append(D)
    d_li.sort()

    ans = 0

    for k in k_li:
        a = bisect.bisect_left(d_li, k)
        ans += min(abs(d_li[a] - k), abs(d_li[a-1] - k))
    print(ans)





if __name__ == '__main__':
    main()
