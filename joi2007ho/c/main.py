import bisect
mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]
    se = set(li)
    ans = 0
    from itertools import combinations
    for a, b in combinations(list(range(n)), 2):
        p1 = li[a]
        p2 = li[b]
        x3, y3 = p1[0] + (p2[1] - p1[1]), p1[1] - (p2[0] - p1[0])
        p3 = (x3, y3)
        x4, y4 = p2[0] + (p2[1] - p1[1]), p2[1] - (p2[0] - p1[0])
        p4 = (x4, y4)

        if p3 in se and p4 in se:
            ans = max(ans, (x3 - x4)**2 + (y3 - y4)**2)
    print(ans)


if __name__ == '__main__':
    main()
