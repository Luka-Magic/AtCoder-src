n, m = map(int, input().split())
li = list(map(int, input().split()))

dp = [[float('inf')] * (n+1) for _ in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0

for i in range(1, m+1):
    v = li[i-1]
    for j in range(n+1):
        if j < v:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i][j-v] + 1, dp[i-1][j])
print(dp[-1][-1])