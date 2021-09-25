def main():
    mod = 10**9 + 7
    n, l = map(int, input().split())
    dp = [1] + [0] * n
    for i in range(0, n):
        dp[i+1] += dp[i] % mod
        if i+l <= n:
            dp[i+l] += dp[i] % mod
        dp[i] %= mod
    print(dp[-1] % mod)


if __name__ == '__main__':
    main()