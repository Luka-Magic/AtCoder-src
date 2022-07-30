import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    dp = [[0] * 21 for _ in range(n-1)]
    dp[0][li[0]] = 1
    li = li[1:]
    for i in range(n-1):
        v = li[i-1]
        for j in range(0, 21):
            if j - v >= 0:
                dp[i][j] += dp[i-1][j-v]
            if v + j <= 20:
                dp[i][j] += dp[i-1][j+v]
    print(dp[-1][li[-1]])
if __name__ == '__main__':
    main()
