n, l = map(int, input().split())
mod = 10**9+7

dp = [1] + [0]*n

for i in range(1, n+1):
    if i < l:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-l] % mod
print(dp[-1] % mod)
