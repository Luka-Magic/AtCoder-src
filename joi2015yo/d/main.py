import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    d_li = [int(input()) for _ in range(n)]
    c_li = [int(input()) for _ in range(m)]

    dp = [[inf]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1, m+1):
        c = c_li[i-1]
        for j in range(n+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + c*d_li[j-1])
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
