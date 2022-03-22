mod = 10**9 + 7
s = input()
dp = [[0] * len(s) for _ in range(8)]
cho = list('chokudai')

for i in range(len(s)):
    if s[i] == cho[0]:
        dp[0][i] = 1

for i in range(1, 8):
    c = 0
    for j in range(len(s)):
        if s[j] == cho[i-1]:
            c += dp[i-1][j] % mod
        elif s[j] == cho[i]:
            dp[i][j] = c % mod
print(sum(dp[-1]) % mod)