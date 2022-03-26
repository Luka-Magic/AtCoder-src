import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, k = map(int, input().split())
    li = list(set(map(int, input().split())))
    li.sort()
    import bisect
    k1 = bisect.bisect_left(li, 0)
    k2 = bisect.bisect_right(li, 0)
    m = k1
    z = k2 - k1
    p = n - k2
    M = li[:m]
    P = li[n-p:]
    from itertools import groupby
    M_r = [[key,len(list(group))] for key,group in groupby(M)]
    P_r = [[key,len(list(group))] for key,group in groupby(P)]
    n = 0    


if __name__ == '__main__':
    main()
