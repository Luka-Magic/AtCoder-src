mod = 10**9 + 7
inf = float('inf')

def main():
    s = list(input())

    p = [1]
    for i in range(len(s)):
        p.append((p[-1]*10) % 13)
    dp = [[0]*13 for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i, k in enumerate(s[::-1]):
        if k != '?':
            k = int(k)
            q = (k * p[i]) % 13
            for a in range(13):
                dp[i+1][(a+q) % 13] = (dp[i+1][(a+q) % 13] + dp[i][a]) % mod
        else:
            for b in range(10):
                q = (b * p[i]) % 13
                for a in range(13):
                    dp[i+1][(a+q) % 13] = (dp[i+1][(a+q) %
                                                   13] + dp[i][a]) % mod
    print(dp[-1][5] % mod)


if __name__ == '__main__':
    main()
