import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n, m, k = map(int, input().split())
    ans = 0
    dp = [[0] * (k) for _ in range(n)]

    for i in range(m):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(k):
            for l in range(max(j-m, 0), j):
                dp[i][j] += dp[i-1][l]
                dp[i][j] %= mod
    for i in range(k):
        ans += dp[-1][i]
        ans %= mod

    print(ans % mod)



if __name__ == '__main__':
    main()