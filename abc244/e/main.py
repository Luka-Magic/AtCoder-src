import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n, m, K, s, T, x = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    dp = [[[0]*n for _ in range(2)] for _ in range(K+1)]
    dp[0][0][s-1] = 1

    for k in range(1, K+1):
        for e in range(2):
            for i in range(n):
                va = dp[k-1][e][i]
                if va != 0:
                    to = g[i]
                    for t in to:
                        if t != x-1:
                            dp[k][e][t] += va % mod
                            dp[k][e][t] %= mod
                        else:
                            dp[k][(e+1) % 2][t] += va % mod
                            dp[k][(e+1) % 2][t] %= mod
    print(dp[-1][0][T-1] % mod)

if __name__ == '__main__':
    main()
