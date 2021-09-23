import sys
input = sys.stdin.readline


def main():
    mod = 10**9+7
    s = input()
    n = len(s)
    c = 'chokudai'
    dp = [[0] * (n+1) for _ in range(9)]
    for i in range(n+1):
        dp[0][i] = 1

    for i in range(1, 9):
        for j in range(1, n+1):
            if s[j-1] != c[i-1]:
                dp[i][j] = dp[i][j-1]
            elif s[j-1] == c[i-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
