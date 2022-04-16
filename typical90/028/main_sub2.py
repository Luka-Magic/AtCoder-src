from collections import Counter
from itertools import accumulate


def main():
    n = int(input())
    li = [[0] * 1001 for _ in range(1001)]
    for _ in range(n):
        lx, ly, rx, ry = map(int, input().split())
        li[ly][lx] += 1
        li[ry][rx] += 1
        li[ly][rx] -= 1
        li[ry][lx] -= 1

    ans_l = []
    ans = []
    for l in li:
        ans_l.append(list(accumulate(l)))
    ans_l = [list(i) for i in zip(*ans_l)]
    for l in ans_l:
        ans.extend(accumulate(l))

    c = Counter(ans)
    for i in range(1, n+1):
        print(c[i])


if __name__ == '__main__':
    main()
