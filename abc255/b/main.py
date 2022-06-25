import sys
input = sys.stdin.readline

import math

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    li = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i, p in enumerate(li):
        if i+1 in p:
            continue
        min_ = inf
        for a in A:
            s = li[a-1]
            d = math.sqrt((s[0] - p[0])**2 + (s[1] - p[1])**2)
            min_ = min(min_, d)
    
        ans = max(min_, ans)
    print(ans)




if __name__ == '__main__':
    main()
