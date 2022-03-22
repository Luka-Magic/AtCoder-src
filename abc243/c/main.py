from itertools import groupby
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    S = list(input())
    li2 = dict()
    for i in range(n):
        x, y, s = li[i][0], li[i][1], S[i]
        if y not in li2:
            li2[y] = [[x, s]]
        else:
            li2[y].append([x, s])

    for l in li2.values():
        l_max, r_min = -float('inf'), float('inf')
        for i, v in l:
            if v == 'R':
                r_min = min(r_min, i)
            else:
                l_max = max(l_max, i)
        if r_min < l_max:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()
