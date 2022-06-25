import sys
input = sys.stdin.readline
from itertools import combinations

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())

    li = [tuple(map(int, input().split())) for _ in range(m)]

    li = set(li)

    ans = 0
    for i in range(2**n):
        c = 0
        k = []
        for j in range(n):
            if (i >> j) & 1:
                k.append(j+1)
                c += 1
        for p in combinations(k, 2):
            if p not in li:
                break
        else:
            ans = max(ans, c)
    print(ans)

if __name__ == '__main__':
    main()
