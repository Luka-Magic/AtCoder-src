import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    dp = [[0] * 10 for _ in range(n)]
    dp[0][li[0]] = 1
    dic = {}
    for i in range(10):
        for j in range(10):
            dic[(i, j)] = (i + j) % 10, (i * j) % 10

    for i, k in enumerate(li):
        if i == 0:
            continue
        for t in range(10):
            p = dp[i-1][t] % mod
            a, b = dic[(t, k)]
            dp[i][a] += p
            dp[i][b] += p
            dp[i][a] %= mod
            dp[i][b] %= mod

    for i in dp[-1]:
        print(i % mod)

if __name__ == '__main__':
    main()
