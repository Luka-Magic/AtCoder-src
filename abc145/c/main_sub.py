import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    from itertools import permutations
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in permutations(list(range(n)), n):
        d = 0
        for j in range(n-1):
            a = i[j]
            b = i[j+1]
            d += math.sqrt((li[b][0] - li[a][0])**2 + (li[b][1] - li[a][1])**2)
        ans.append(d)
    print(sum(ans) / len(ans))


if __name__ == '__main__':
    main()
