mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    masu = [list(input()) for _ in range(5)]
    cost = [[0] * n for _ in range(3)]
    for i in range(5):
        for j in range(n):
            if masu[i][j] == 'R':
                cost[0][j] += 1
            if masu[i][j] == 'B':
                cost[1][j] += 1
            if masu[i][j] == 'W':
                cost[2][j] += 1
    for i in range(3):
        for j in range(n):
            cost[i][j] = 5 - cost[i][j]
    dp = [[0] * n for _ in range(3)]
    for i in range(3):
        dp[i][0] = cost[i][0]

    for j in range(1, n):
        for i in range(3):
            dp[i][j] = min(dp[(i+1)%3][j-1], dp[(i+2)%3][j-1]) + cost[i][j]
    
    ans = inf
    for i in range(3):
        ans = min(dp[i][-1], ans)
    
    print(ans)


if __name__ == '__main__':
    main()
