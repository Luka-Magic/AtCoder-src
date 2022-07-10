import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))

    dp = [[0] * 9 for _ in range(n)]

    for i, l in enumerate(li):
        if l >= n:
            continue
        dp[l-1][i] = i + 1

    for i in range(n):
        for j in range(9):
            if dp[i][j] == 0:
                continue
            for k in range(9):
                if i + li[k] >= n:
                    continue
                dp[i + li[k]][k] = max(dp[i][j] * 10 + k + 1, dp[i + li[k]][k])
    ans = max(dp[-1])
    for d in dp:
        print(*d)
    print(ans)

if __name__ == '__main__':
    main()
