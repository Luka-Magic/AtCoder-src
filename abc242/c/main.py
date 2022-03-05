import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n = int(input())
    ans = 0
    dp = [[0] * 9 for _ in range(n)]
    for i in range(9):
        dp[0][i] = 1
    for k in range(1, n):
        for i in range(9):
            if i == 0:
                dp[k][i] = (dp[k-1][i] + dp[k-1][i+1]) % mod
            elif i == 8:
                dp[k][i] = (dp[k-1][i] + dp[k-1][i-1]) % mod
            else:
                dp[k][i] = (dp[k-1][i+1] + dp[k-1][i] + dp[k-1][i-1]) % mod
    print(sum([i % mod for i in dp[-1]]) % mod)

if __name__ == '__main__':
    main()
