import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    D, n = map(int, input().split())
    d_li = [int(input()) for _ in range(D)]
    f = [list(map(int, input().split())) for _ in range(n)]

    y_set = set()
    for j in range(n):
        if f[j][0] <= d_li[0] <= f[j][1]:
            y_set.add(j)

    dp = [[0] * n for _ in range(D)]
    for i in range(1, D):
        n_set = set()
        tem = d_li[i]
        for j in range(n):
            if f[j][0] <= tem <= f[j][1]:
                n_set.add(j)
        for yes in y_set:
            for tod in n_set:
                dp[i][tod] = max(dp[i][tod], dp[i-1][yes] +
                                    abs(f[tod][2] - f[yes][2]))
        y_set = n_set
    print(max(dp[-1]))
    # for l in dp:
    #     print(*l)


if __name__ == '__main__':
    main()
