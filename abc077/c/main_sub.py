import sys
input = sys.stdin.readline

import  bisect
from itertools import accumulate

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

    b_li = []
    
    for i in range(n):
        b = bisect.bisect_left(A, B[i])
        b_li.append(b)
    
    b_c = list(accumulate(b_li))

    ans = 0

    for i in range(n):
        c = bisect.bisect_left(B, C[i])
        if c == 0:continue
        ans += b_c[c-1]

    print(ans)

if __name__ == '__main__':
    main()
