import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    dic = {}
    for _ in range(k):
        k, v = map(int, input().split())
        dic[k-1] = v-1

    dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
    for i in range(3):
        if 0 not in dic.keys():
            dp[0][i][0] = 1
        else:
            dp[0][dic[0]][0] = 1
    for i in range(1, n):
        for j in range(3):
            for k in range(2):
                if k == 1:
                    dp[i][j][k] = dp[i-1][j][k-1]
                else:
                    for jj in range(3):
                        if jj == j:continue
                        for kk in range(2):
                            dp[i][j][k] += dp[i-1][jj][kk]
                            dp[i][j][k] %= 10000
                dp[i][j][k] %= 10000
        if i in dic.keys():
            v = dic[i]
            for j in range(3):
                if v == j:continue
                for k in range(2):
                    dp[i][j][k] = 0
    ans = 0
    for j in range(3):
        for k in range(2):
            ans += dp[-1][j][k] % 10000
    print(ans % 10000)


if __name__ == '__main__':
    main()
