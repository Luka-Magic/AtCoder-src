import bisect
mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    lx = list(map(lambda x:x[0], li))
    lx.sort()
    li.sort(key=lambda x:x[0])
    ans = 0
    from itertools import combinations
    for a, b in combinations(list(range(n)), 2):
        p1 = li[a]
        p2 = li[b]
        x3, y3 = p1[0] + (p2[1] - p1[1]), p1[1] - (p2[0] - p1[0])
        p3 = [x3, y3]
        x4, y4 = p2[0] + (p2[1] - p1[1]), p2[1] - (p2[0] - p1[0])
        p4 = [x4, y4]

        p, q = bisect.bisect_left(lx, x3), bisect.bisect_right(lx, x3)
        flag = False
        for j in range(p, q):
            if li[j][0] == x3 and li[j][1] == y3:
                flag = True
        if not flag:continue

        flag = False
        r, s = bisect.bisect_left(lx, x4), bisect.bisect_right(lx, x4)
        for j in range(r, s):
            if li[j][0] == x4 and li[j][1] == y4:
                flag = True
        if not flag:
            continue
        ans = max(ans, (x3 - x4)**2 + (y3 - y4)**2)
    print(ans)


        
        



if __name__ == '__main__':
    main()
