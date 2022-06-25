import bisect
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    X = sum([a-A[0] for a in A])
    c = 1
    a_c = A[0]
    d_c = -n + 2
    X_c = X
    li = [[a_c, X_c, d_c]]
    for i, a in enumerate(A):
        if i == 0:
            continue
        if a == a_c:
            c += 1
            d_c += 2
            continue
        if c >= 2:
            a_, X_, d_ = li.pop()
            for _ in range(c):
                li.append([a_, X_, d_c])
            c = 1
        X = X_c - (a_c - a) * d_c
        d_c += 2
        li.append([a, X, d_c])
        a_c = a
        X_c = X
    if c >= 2:
        a_, X_, d_ = li.pop()
        for _ in range(c):
            li.append([a_, X_, d_c])
        c = 1
    for i in range(q):
        x = int(input())
        idx = bisect.bisect_right(A, x)
        if idx > 0:
            print(li[idx-1][1] + (x - li[idx-1][0])*li[idx-1][2])
        else:
            print(li[0][1] + (li[0][0] - x) * n)
if __name__ == '__main__':
    main()
