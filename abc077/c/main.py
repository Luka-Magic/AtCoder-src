from itertools import accumulate
import bisect
import sys
input = sys.stdin.readline


mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()

    ans = 0

    for i in range(n):
        b = B[i]
        a_i = bisect.bisect_left(A, b)
        c_i = bisect.bisect_right(C, b)
        ans += a_i * (n - c_i)

    print(ans)


if __name__ == '__main__':
    main()
