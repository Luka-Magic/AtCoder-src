n = int(input())
for _ in range(n):
    x = list(input())
    y = list(input())
    # dp[i][j]: xi, yjまでの共通部分
    dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
    for i in range(1, 1+len(x)):
        for j in range(1, 1+len(y)):
            if x[i-1] == y[j-1]:
                # dp[i][j] = max(dp[i-1][j] + 1, dp[i][j-1] + 1)
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(dp[-1][-1])
    for l in dp:
        print(*l)
