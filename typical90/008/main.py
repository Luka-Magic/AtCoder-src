def main():
    n = int(input())
    S = input()
    at = 'atcoder'
    l = len(at)
    mod = 10**9 + 7
    dp = [[1] * (n+1)] + [[0] * (n+1) for _ in range(l)]
    for i in range(1, l+1):
        for j in range(1, n+1):
            if at[i-1] == S[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
            else:
                dp[i][j] = dp[i][j-1]

    print(dp[-1][-1])


if __name__ == '__main__':
    main()