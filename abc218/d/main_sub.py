import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    dic = {}
    for l in li:
        x, y = l
        if x not in dic:
            dic[x] = {y}
        else:
            dic[x].add(y)
    x_l = dic.keys()
    from itertools import combinations
    ans = 0
    for x1, x2 in combinations(x_l, 2):
        k = dic[x1]
        t = dic[x2]
        s = k & t
        s_n = len(s)
        ans += (s_n * (s_n-1)) // 2
    print(ans)

if __name__ == '__main__':
    main()
