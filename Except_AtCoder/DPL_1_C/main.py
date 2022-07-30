N, W = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        v, w = li[i-1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], max(dp[i][j-w] + v, dp[i-1][j-w] + v))
print(dp[-1][-1])