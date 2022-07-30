n, w = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(w+1):
        v, w_ = li[i-1]
        if j < w_:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w_] + v, dp[i-1][j])
print(dp[-1][-1])
