from itertools import groupby
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
    ans = 0
    for j in range(k):
        rl = [[key, len(list(group))]
              for key, group in groupby([t[i] for i in range(j, n, k)])]
        for v, c in rl:
            q = (c+1) // 2
            if v == 'r':
                ans += p * q
            elif v == 's':
                ans += r * q
            elif v == 'p':
                ans += s * q
    print(ans)

if __name__ == '__main__':
    main()
