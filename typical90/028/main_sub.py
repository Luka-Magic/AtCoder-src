from collections import Counter
import itertools


def main():
    n = int(input())
    li = [[0] * 1001 for _ in range(1001)]
    for _ in range(n):
        lx, ly, rx, ry = map(int, input().split())
        for i in range(ly, ry):
            li[i][lx] += 1
            li[i][rx] -= 1
    ans = []

    for l in li:
        k = [l[0]]
        for i in l[1:]:
            k.append(k[-1] + i)
        ans.extend(k)
    c = Counter(ans)
    for i in range(1, n+1):
        print(c[i])


if __name__ == '__main__':
    main()
