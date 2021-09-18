from itertools import permutations


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    no = set()
    for _ in range(m):
        a, b = map(int, input().split())
        no.add((a-1, b-1))
        no.add((b-1, a-1))
    ans = 100000000
    t = 100000000
    flag = False
    for p in permutations([i for i in range(n)], n):
        for k in range(1, n):
            if ((p[k-1], p[k]) in no) or ((p[k], p[k-1]) in no):
                break
        else:
            flag = True
            t = 0
            for i, r in enumerate(p):
                t += li[r][i]
        ans = min(ans, t)
    if flag:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
